from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from .models import User, Note
from .forms import RegForm


# Create your views here.
def home_page(request):
    return render(request, template_name='home_page.html')


def reg_page(request):
    if request.method == "GET":
        form = RegForm()
    else:
        form = RegForm(request.POST)
        data = request.POST
        if form.is_valid():
            if form.check_password() and form.check_username():
                new_user = User()
                new_user.create_user(data.get("username"), data.get("first_name"),
                                     data.get("last_name"), data.get("email"), data.get("password1"))
                return redirect(home_page)
            elif not form.check_username():
                form.add_error("username", "Длина имени должна быть минимум 2 символа")
            elif not form.check_password():
                form.add_error("password1", 'Пароли должны совпадать')
        else:
            form.add_error(None, "Заполните всю форму")
    context = {'form': form}
    return render(request, 'reg_page.html', context)


def login_page(request):
    if request.method == "GET":
        return render(request, "login_page.html")
    else:
        data = request.POST
        context = {'page': 'login'}
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                context['response'] = "Пользователь с таким логином и паролем не найден"
                return render(request, 'get_back.html', context=context)
            login(request, user)
            return redirect(home_page)
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")


def logout_page(request):
    logout(request)
    return redirect(home_page)


@login_required
def change_password_page(request):
    if request.method == "GET":
        return render(request, "change_password_page.html")
    data = request.POST
    context = {'page': 'change_password'}
    try:
        user = authenticate(request, username=request.user.username, password=data['old_password'])
        if user is None:
            context['response'] = "Введён неверный пароль"
            return render(request, 'get_back.html', context=context)
        elif data['new_password1'] != data['new_password2']:
            context['response'] = "Пароли должны совпадать"
            return render(request, 'get_back.html', context=context)
        user = request.user
        user.set_password(data['new_password1'])
        user.save()
        return redirect(home_page)
    except KeyError:
        context['response'] = "заполните все поля"
        return render(request, 'get_back.html', context=context)


def add_note_page(request):
    if request.method == "GET":
        return render(request, 'add_note_page.html')
    request.user.new_note(request.POST)
    return redirect(home_page)


def notes_page(request):
    notes = Note.objects.filter(User=request.user.id).all()
    return render(request, 'notes_page.html', context={'notes': notes})

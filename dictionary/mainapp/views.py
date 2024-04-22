from django.shortcuts import render, redirect


# Create your views here.
def index_page(request):
    return render(request, template_name='index.html')


def add_word_page(request):
    if request.method == 'GET':
        return render(request, template_name='add_word.html')
    else:
        print(request.POST)
        with open(r"dictionary.txt", "a") as file:
            file.write(f"{request.POST['word1']} - {request.POST['word2']}\n")
        return redirect(index_page)


def read_from_file():
    with open(r"dictionary.txt", "r", encoding="utf-8") as file:
        contents = [i.strip() for i in file.readlines()]
        words1 = []
        words2 = []
        for line in contents:
            word1, word2 = line.split(" - ")
            words1.append(word1)
            words2.append(word2)
    return zip(words1, words2)


def words_list_page(request):
    context = {'words': read_from_file()}
    return render(request, template_name='words_list.html', context=context)


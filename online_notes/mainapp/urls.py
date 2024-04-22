from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name="home"),
    path("home", views.home_page, name="home"),
    path("home/", views.home_page, name="home"),
    path("reg", views.reg_page, name="reg"),
    path("reg/", views.reg_page, name="reg"),
    path("login", views.login_page, name="login"),
    path("login/", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("logout/", views.logout_page, name="logout"),
    path("change_password", views.change_password_page, name="change_password"),
    path("change_password/", views.change_password_page, name="change_password"),
    path("add_note", views.add_note_page, name="add_note"),
    path("add_note/", views.add_note_page, name="add_note"),
    path("notes", views.notes_page, name="notes"),
    path("notes/", views.notes_page, name="notes"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

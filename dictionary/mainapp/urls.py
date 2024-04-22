from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_page, name='index'),
    path('home', views.index_page, name='index'),
    path('home/', views.index_page, name='index'),
    path('add_word', views.add_word_page, name='add_word'),
    path('add_word/', views.add_word_page, name='add_word'),
    path('words_list', views.words_list_page, name='words_list'),
    path('words_list/', views.words_list_page, name='words_list'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('goods', views.goods_api, name='goods_api'),
    path('goods/', views.goods_api, name='goods_api'),
    path('new_good', views.new_good_view, name='new_good'),
    path('new_good/', views.new_good_view, name='new_good'),
    path('get_token', views.get_token_view, name='get_token'),
    path('get_token/', views.get_token_view, name='get_token'),
]

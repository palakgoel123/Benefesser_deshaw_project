from django.urls import include, re_path
from django.urls import include, path
from . import views


# Code for video 7
urlpatterns = [
    path('profile/', views.profile_page, name='profile'),
    re_path(r'/addmoney/', views.addmoney, name='add_money'),
    re_path(r'^updated/$', views.adding, name='adding'),
]
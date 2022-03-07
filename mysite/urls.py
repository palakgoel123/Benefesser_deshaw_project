from django.contrib import admin
from django.urls import path
from . import views


# Code for video 7
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('UserRegistration/', views.user_r, name='user_r'),
    path('CharityRegistration/', views.charity_r, name='charity_r'),

]
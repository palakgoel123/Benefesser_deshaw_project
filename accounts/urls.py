from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('UserRegistration/', views.user_r, name='user_r'),
    path('login', views.loginPage, name='loginPage'),
    path('loginc', views.logincharity, name='logincharity'),
    path('CharityRegistration/', views.charity_r, name='charity_r'),
    path('logout/', views.logout_user, name="logout_user"),
    path('payment/',views.payment,name="payment"),
    path('payment_update/',views.donating,name="subtracting"),
]

# superuser: Admin, admin123@gmail.com, Admin123

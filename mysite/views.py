from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def user_r(request):
    return render(request, 'user_registration.html')


def charity_r(request):
    return render(request, 'charity_registration.html')


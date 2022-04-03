from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html')



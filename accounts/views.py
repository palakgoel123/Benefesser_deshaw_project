from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import auth
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .forms import CreateCharityForm
from UserPage.models import balance

def user_r(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            USER = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            instance = balance(user = USER, balance = 0)
            instance.save()
            return redirect('/login')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'user_registration.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/explore')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    auth.logout(request)
    return redirect('/')


def charity_r(request):
    formc = CreateCharityForm()
    if request.method == 'POST':
        formc = CreateCharityForm(request.POST)
        if formc.is_valid():
            saved_user=formc.save()
            username = formc.cleaned_data.get('username')
            password = formc.cleaned_data.get('password1')
            saved_user.set_password(password)
            saved_user.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('/loginc')
        else:
            print(formc.errors)

    context = {'formc': formc}
    return render(request, 'Charity_registration.html', context)


def logincharity(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userc = authenticate(request, username=username, password=password)
        if userc is not None:
            login(request, userc)
            return redirect('/explore')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'loginc.html', context)

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator


class CreateUserForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    name = forms.CharField(max_length=101)
    email = forms.EmailField()
    password1 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['name', 'phone', 'username', 'email', 'password1', 'password2']


class CreateCharityForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    name = forms.CharField(max_length=101)
    year = forms.CharField(max_length=4)
    certificate= forms.ImageField()
    location = forms.CharField(max_length=101)
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['name', 'year', 'phone', 'location', 'certificate', 'username', 'email', 'password1', 'password2']

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from explore.models import Charity


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

    class Meta:
        widgets = {'password1': forms.PasswordInput(), 'password2': forms.PasswordInput()}
        model = Charity
        fields = ['name', 'year', 'location', 'charity_theme', 'pic_link', 'rating', 'certificate', 'username', 'email',
                  'password1', 'password2']

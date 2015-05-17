__author__ = 'A.Hosseini'

from django import forms
from .models import Signup
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class SignupForm(forms.Form):

    class Meta:
        model = Signup
        fields = '__all__'


class CaptchaForm(forms.Form):
    captcha = CaptchaField()
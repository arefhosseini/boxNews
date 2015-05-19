__author__ = 'A.Hosseini'

from django import forms
from .models import Signup, varzeshComment, Profile, musicComment, movieComment, gameComment
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


class ProfileForm(forms.Form):

    class Meta:
        model = Profile
        fields = '__all__'


class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class varzeshCommentForm(forms.ModelForm):
    class Meta:
        model = varzeshComment
        fields = '__all__'


class gameCommentForm(forms.ModelForm):
    class Meta:
        model = gameComment
        fields = '__all__'


class musicCommentForm(forms.ModelForm):
    class Meta:
        model = musicComment
        fields = '__all__'


class movieCommentForm(forms.ModelForm):
    class Meta:
        model = movieComment
        fields = '__all__'
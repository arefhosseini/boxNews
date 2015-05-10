__author__ = 'A.Hosseini'

from django.forms import ModelForm
from .models import Signup


class SignupForm(ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'
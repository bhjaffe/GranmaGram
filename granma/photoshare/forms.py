from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserProfileForm(forms.Form):
    full_name = forms.CharField(max_length=35)
    email = forms.EmailField()

class NewCircleForm(forms.Form):
    full_name = forms.CharField(max_length=35)
    username = forms.CharField(max_length=35)
    password = forms.CharField(widget=forms.PasswordInput)

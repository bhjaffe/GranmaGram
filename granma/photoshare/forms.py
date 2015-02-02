from django.forms import ModelForm
from photoshare.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

TO_HIDE_ATTRS = {'class': 'hidden'}
class UserProfileForm(forms.Form):
    full_name = forms.CharField(max_length=35)
    email = forms.EmailField()

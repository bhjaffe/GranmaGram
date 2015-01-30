from django.forms import ModelForm
rom photoshare.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
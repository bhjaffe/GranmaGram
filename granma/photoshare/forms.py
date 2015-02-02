from django.forms import ModelForm
from photoshare.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['sku'].widget.attrs['readonly'] = True
    #
    #     def clean_sku(self):
    #         instance = getattr(self, 'instance', None)
    #         if instance and instance.pk:
    #             return instance.sku
    #         else:
    #             return self.cleaned_data['sku']
    class Meta:
        model = UserProfile
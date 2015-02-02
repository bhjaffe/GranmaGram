from django import forms

class UserProfileForm(forms.Form):
    full_name = forms.CharField(max_length=35)
    email = forms.EmailField()

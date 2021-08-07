from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = AppUser
#         fields = ('profileImage',)

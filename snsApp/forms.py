from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username', 'class':'register-input'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password', 'class':'register-input'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email', 'class':'register-input'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name', 'class':'register-input'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last name', 'class':'register-input'}), label='')


    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = AppUser
#         fields = ('profileImage',)

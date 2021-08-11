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

class UserProfileForm(forms.ModelForm):
    # YEARS= [x for x in range(1940,2022)]
    dateOfBirth = forms.DateField(widget=forms.SelectDateWidget(years=range(1940,2022), attrs={'placeholder':'DOB(mm/dd/yyyy)', 'class':'register-input date-birth'}), label='date of birth')
    ocupation = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'ocupation', 'class':'register-input'}), label='')
    organization = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'organization', 'class':'register-input'}), label='')
    profileImage = forms.ImageField(label='profile image', required=False)
    class Meta:
        model = AppUser
        fields = ('dateOfBirth', 'ocupation', 'organization', 'profileImage')

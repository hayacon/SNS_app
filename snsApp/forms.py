from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User

# Form for singup
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username', 'class':'register-input'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password', 'class':'register-input'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email', 'class':'register-input'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name', 'class':'register-input'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last name', 'class':'register-input'}), label='')

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)

# Form for singup
class UserProfileForm(forms.ModelForm):
    # YEARS= [x for x in range(1940,2022)]
    dateOfBirth = forms.DateField(widget=forms.SelectDateWidget(years=range(1940,2022), attrs={'placeholder':'DOB(mm/dd/yyyy)', 'class':'register-input date-birth'}), label='date of birth')
    ocupation = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'ocupation', 'class':'register-input'}), label='')
    organization = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'organization', 'class':'register-input'}), label='')
    profileImage = forms.ImageField(label='profile image', required=False)
    class Meta:
        model = AppUser
        fields = ('dateOfBirth', 'ocupation', 'organization', 'profileImage')

# Forms for user to update their profiles
class UserFormUpdate(forms.ModelForm):
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class':'profile-update', "id":"profile-update"}), label='email:')
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'profile-update'}), label='first name')
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'profile-update'}), label='last name')

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')

class UserProfileFormUpdate(forms.ModelForm):
    ocupation = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'profile-update'}), label='ocupation')
    organization = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'profile-update'}), label='organization')
    bio = forms.CharField(required=False, widget=forms.Textarea(), label='bio')
    profileImage = forms.ImageField(label='profile image', required=False)
    class Meta:
        model = AppUser
        fields = ('ocupation', 'organization', 'bio', 'profileImage')

#Form to create a new post
class NewPostForm(forms.Form):
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'what you reckon?'}), label='', help_text="word limit : 500")
    media = forms.ImageField(label="image", required=False)
    user = forms.CharField(widget=forms.HiddenInput(), required=False)

    def save(self, user, time):
        text = self.cleaned_data['text']
        media = self.cleaned_data['media']
        post = Post(user=user, postDate=time, text=text,likes=0, media=media,)
        post.save()

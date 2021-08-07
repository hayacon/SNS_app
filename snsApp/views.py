from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # profile.save()
            registered=True
    else:
        user_form = UserForm()
        # profile_form = UserProfileForm()

    # return render(request, 'snsApp/signup.html', {'user_form': user_form, 'profile_form':profile_form, 'registered':registered})
    return render(request, 'snsApp/signup.html', {'user_form': user_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/signup')
            else:
                return HttpResponse("Your account is disable")
        else:
            return HttpResponse("Invalid login")
    return render(request, 'snsApp/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../signup')

from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
from datetime import datetime

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered=True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'snsApp/signup.html', {'user_form': user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disable")
        else:
            return HttpResponse("Invalid login")
    return render(request, 'snsApp/login.html', {})

def user_logout(request):
    logout(request)
    return render(request, "snsApp/logout.html")

def sidebar(request):
    user = request.user
    if user.is_authenticated:
        user_profile = AppUser.objects.get(user=user)
        if user_profile.profileImage:
            image_url = user_profile.profileImage.url
        else:
            image_url = ''
        return render(request, "snsApp/home_base.html", {'user':user, 'user_profile':user_profile, 'img_url':image_url})
    else:
        return render(request, "snsApp/home_base.html")

@login_required
def user_profile(request):
    user = request.user
    user_profile = AppUser.objects.get(user=user)
    if user_profile.profileImage:
        image_url = user_profile.profileImage.url
        old_image_url = user_profile.profileImage.path
    else:
        image_url= None
        old_image_url = None
    if user.is_authenticated:
        if request.method == "POST":
            print("old : ", old_image_url)
            user_form = UserFormUpdate(request.POST or None, instance=user)
            user_profile_form = UserProfileFormUpdate(request.POST or None, request.FILES, instance=user_profile, initial={ "ocupation":user_profile.ocupation, "organization":user_profile.organization})
            if user_form.is_valid() and user_profile_form.is_valid():
                user_form.save()
                if user_profile.profileImage:
                    new_image_url = user_profile.profileImage.path
                    print("new : ", new_image_url)
                    if old_image_url==new_image_url:
                        user_profile_form.save()
                    elif old_image_url==None:
                        user_profile_form.save()
                    else:
                        os.remove(old_image_url)
                        user_profile_form.save()
                else:
                    user_profile_form.save()
                return HttpResponseRedirect('/profile')
        else:
            user_form = UserFormUpdate(instance=user)
            user_profile_form = UserProfileFormUpdate(instance=user_profile)
    else:
        return HttpResponseRedirect('/login')

    return render(request, "snsApp/user_profile.html", {"user":user, "user_profile":user_profile, "img_url":image_url, "user_form":user_form, "profile_form":user_profile_form})

@login_required
def user_home(request):
    user = request.user
    if user.is_authenticated:
        user_profile = AppUser.objects.get(user=user)
        img_url = user_profile.profileImage.url
        if request.method=="POST":
            post_form = NewPostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post_form.save(user=user, time=datetime.now())
        else:
            post_form = NewPostForm()
    else:
        return HttpResponseRedirect('/login')
    return render(request, "snsApp/user_home.html", {"user_profile":user_profile, "img_url":img_url, "post_form":post_form})

def search_user(request):
    if request.method == "POST":
        search = request.POST['user-search']
        if search:
            result=User.objects.filter(username__contains=search)
            images = []
            for user in result:
                profile_result=AppUser.objects.get(user=user)
                if profile_result.profileImage:
                    profile_img = profile_result.profileImage.url
                    images.append(profile_img)
                else:
                    images.append(None)
            search_result = zip(result, images)
            return render(request, "snsApp/search_user.html",{'search_result':search_result})
        else:
            return render(request, 'snsApp/search_user.html')
    else:
        return HttpResponseRedirect("/")

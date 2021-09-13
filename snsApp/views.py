from django.shortcuts import render
from .models import *
from .forms import *
from .serializers import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status, generics, mixins
from rest_framework.views import APIView

#view for register a new user
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid(): #form validation
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

#view for user login
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

#view for user logout
def user_logout(request):
    logout(request)
    return render(request, "snsApp/logout.html")

#view for user to see and update their profile information
@login_required
def user_profile(request):
    user = request.user
    if user.is_authenticated:
        #get user's basic informations
        user_profile = AppUser.objects.get(user=user)
        if user_profile.profileImage:
            image_url = user_profile.profileImage.url
            old_image_url = user_profile.profileImage.path
        else:
            image_url= None
            old_image_url = None

        if request.method == "POST":
            #update user's information
            user_form = UserFormUpdate(request.POST or None, instance=user)
            user_profile_form = UserProfileFormUpdate(request.POST or None, request.FILES, instance=user_profile, initial={ "ocupation":user_profile.ocupation, "organization":user_profile.organization})
            if user_form.is_valid() and user_profile_form.is_valid():#form validation
                user_form.save()
                if user_profile.profileImage:
                    new_image_url = user_profile.profileImage.path
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

#view for home page pf loggedd in user
@login_required
def main_user_home(request):
    user = request.user
    if user.is_authenticated:
        user_profile = AppUser.objects.get(user=user)
        if user_profile.profileImage:
            img_url = user_profile.profileImage.url
        else:
            img_url = None
        if request.method=="POST":
            #create a status update
            post_form = NewPostForm(request.POST, request.FILES)
            if post_form.is_valid(): #form validation
                post_form.save(user=user, time=datetime.now())
        else:
            post_form = NewPostForm()

        #get all user's post
        post = Post.objects.filter(user=user).order_by('-postId')
        #get a count of user's followers and followings
        follower_count = Follower.objects.filter(user=request.user).count()
        following_count = Follower.objects.filter(follower=request.user).count()

    else:
        return HttpResponseRedirect('/login')

    return render(request, "snsApp/user_home.html", {"user_profile":user_profile, "img_url":img_url, "post_form":post_form, "posts":post, "follower_count":follower_count, "following_count":following_count})

#api view for all user home
class UserHome(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "snsApp/user.html"

    def get(self, request, username):#get user's information
        if Follower.objects.filter(user=username, follower=request.user):
            following=True
        else:
            following=False

        queryset = User.objects.get(username=username)
        user = UserSerializer(queryset)
        if queryset.profile.profileImage:
            img_url = user.data['profile']['profileImage']
        else:
            img_url = None

        follower_count = Follower.objects.filter(user=username).count()
        following_count = Follower.objects.filter(follower=username).count()

        return Response({"subuser":queryset, "user_profile": user.data['profile'], "img_url": img_url, "posts":user.data['posts'], "following":following, "follower_count":follower_count, "following_count":following_count})

    def post(self, request, username):
        queryset = User.objects.get(username=username)
        user = UserSerializer(queryset)
        if queryset.profile.profileImage:
            img_url = user.data['profile']['profileImage']
        else:
            img_url = None

        follower_count = Follower.objects.filter(user=username).count()
        following_count = Follower.objects.filter(follower=username).count()

        if request.method=="POST": #follow and unfollow user
            #check if user is following another user or not
            if Follower.objects.filter(user=username, follower=request.user):
                Follower.objects.filter(user=request.data['user'], follower=request.user).delete()
                following=False
            else:
                post_query = Follower.objects.all()
                room_name =''
                follower_serializer = FollowerSerializer(data=request.data)
                #check if chat room already exist or not
                if Follower.objects.filter(user=request.user, follower=username):
                    room_name = Follower.objects.get(user=request.user, follower=username).chat_room
                else:
                    #create a new chat room name
                    room_name = str(request.user) + '_' + str(username)
                    room_name = str(room_name)
                if follower_serializer.is_valid(): #data alidation 
                    follower_serializer.save(chat_room=room_name)
                    following=True

        return Response({"subuser":queryset, "user_profile": user.data['profile'], "img_url": img_url, "posts":user.data['posts'],"following":following, "follower_count":follower_count, "following_count":following_count})

#view for search users
def user_search(request):
    if request.method == "POST":
        search = request.POST['q']
        if search:
            #return all users that partially match with input
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

#view for get a list of follower and following of a user
def network_list(request):
    if request.method == "GET":
        #get a list and count of user's followers and followings
        follower_list=[]
        followers = Follower.objects.filter(user=request.user)
        for user in followers:
            follower_list.append(user)

        following_list=[]
        followings = Follower.objects.filter(follower=request.user)
        for user in followings:
            following_list.append(user)
        return render(request, "snsApp/network.html", {"follower_list":follower_list, "following_list":following_list})
    else:
        return HttpResponseRedirect("user_home/")

#api view for home feed page
class PostView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'snsApp/home_base.html'

    def get(self, request):
        user = request.user
        queryset = Post.objects.all().order_by('-postId')
        if user.is_authenticated:
            user_profile = AppUser.objects.get(user=user)
            following_list=[]
            followings = Follower.objects.filter(follower=request.user)
            for following in followings:
                following_list.append(following)
            if user_profile.profileImage:
                image_url = user_profile.profileImage.url
            else:
                image_url = None

            return Response({'posts':queryset, 'user_profile':user_profile, 'img_url':image_url, 'user':user,'following_list':following_list})

        return Response({'posts':queryset, 'user_profile':None, 'img_url':None, 'user':user,'following_list':None})

#view for a chat room
def chat_room(request, room_name):
    user_profile = AppUser.objects.get(user=request.user)
    if user_profile.profileImage:
        image_url = user_profile.profileImage.url
    else:
        image_url = ''
    following_list=[]
    followings = Follower.objects.filter(follower=request.user)
    for following in followings:
        following_list.append(following)
    username = str(request.user)
    return render(request, "snsApp/chat_room.html", {'room_name':room_name, "username":username, 'user_profile':user_profile,'img_url':image_url,'following_list':following_list})

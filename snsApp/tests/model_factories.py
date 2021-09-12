import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from ..models import *
from random import randint,choice

class UserFactory(factory.django.DjangoModelFactory):
    username = 'factory'
    email = 'test@factory.com'
    first_name = 'django'
    last_name = 'python'
    password = '123'

    class Meta:
        model = User

class AppUserFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    profileImage = "./static/media/blank.png"
    dateOfBirth = "1993-04-06"
    ocupation = 'framework'
    organization = 'python'
    bio = "hello world, It's django"

    class Meta:
        model = AppUser

class PostFactory(factory.django.DjangoModelFactory):
    postId = 5
    user = factory.SubFactory(UserFactory)
    postDate = "2020-03-20"
    text = "hello world"
    likes = 10
    media = "./static/media/blank.png"

    class Meta:
        model = Post

class FollowerFactory(factory.django.DjangoModelFactory):
    user = 'factory'
    follower = 'follower'
    chat_room = 'room101'

    class Meta:
        model = Follower

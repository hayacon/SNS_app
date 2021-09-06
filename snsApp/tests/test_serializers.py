import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .model_factories import *
from ..serializers import *

# Serializers test
class AppUserSerializerTest(APITestCase):
    appuser = None
    appuserserializer = None

    def setUp(self):
        self.appuser = AppUserFactory.create()
        self.appuserserializer =    AppUserSerializer(instance=self.appuser)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    def test_appUserSerializerHasCorrectFields(self):
        data = self.appuserserializer.data
        self.assertEqual(set(data.keys()),set(['profileImage', 'dateOfBirth', 'ocupation', 'organization', 'bio']))

class PostSerializerTest(APITestCase):
    post = None
    postserializer = None

    def setUp(self):
        self.post = PostFactory.create()
        self.postserializer = PostSerializer(instance=self.post)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    def test_postSerializerHasCorrectFields(self):
        data = self.postserializer.data
        self.assertEqual(set(data.keys()), set(['postId', 'user', 'postDate', 'text', 'media', 'likes']))

class UserSerializerTest(APITestCase):
    user = None
    userserializer = None

    def setUp(self):
        self.user = UserFactory.create()
        self.userserializer = UserSerializer(instance=self.user)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    def test_userSerializerHasCorrectFiedls(self):
        data = self.userserializer.data
        self.assertEqual(set(data.keys()), set(['username', 'first_name', 'last_name','profile','posts']))

class UserPostSerialzerTest(APITestCase):
    user = None
    userpostserializer = None

    def setUp(self):
        self.user = UserFactory.create()
        self.userpostserializer = UserPostSerialzer(instance=self.user)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    def test_userPostSerializerHasCorrectFields(self):
        data = self.userpostserializer.data
        self.assertEqual(set(data.keys()), set(['username', 'posts']))
class FollowerSerializerTest(APITestCase):
    follower = None
    followerserializer = None

    def setUp(self):
        self.follower = FollowerFactory.create()
        self.followerserializer = FollowerSerializer(instance=self.follower)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    def test_followerSerializerHasCorrectFields(self):
        data = self.followerserializer.data
        self.assertEqual(set(data.keys()), set(['user', 'follower', 'chat_room']))

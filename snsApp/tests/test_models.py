import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy
from .model_factories import *
from ..models import *

class AppUserModelTest(TestCase):
    appuser = None

    def setUp(self):
        self.sppuser = AppUserFactory.create()

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

#fix this test
    # def create_AppUser(self, user=User.objects.get(username='a'), profileImage='abc.jpeg', dateOfBirth='08/09/1997', ocupation='teacher', organization='UoL', bio="hello world"):
    #     return AppUser.objects.create(user=user, profileImage=profileImage, dateOfBirth=dateOfBirth, ocupation=ocupation, organization=organization,bio=bio)
    #
    # def test_appUserModelCreation(self):
    #     #test objects creation of Model
    #     appUserModel = self.create_AppUser()
    #     self.assertTrue(appUserModel, AppUser)

    def test_ocupationFieldMaxLength(self):
        #test max_length of 'ocupation' field
        user = AppUser.objects.get(id=1)
        max_length = user._meta.get_field('ocupation').max_length
        self.assertEqual(max_length, 60)

    def test_organizationFieldMaxLength(self):
        #test max_length of 'organization' field
        user = AppUser.objects.get(id=1)
        max_length = user._meta.get_field('organization').max_length
        self.assertEqual(max_length, 100)

    def test_bioFieldMaxLength(self):
        #test max_length of 'bio' field
        user = AppUser.objects.get(id=1)
        max_length = user._meta.get_field('bio').max_length
        self.assertEqual(max_length, 400)



class PostModelTest(TestCase):
    post = None

    def setUp(self):
        self.post = PostFactory.create()

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()


#Unit test for follower model
class FollowerModelTest(TestCase):
    follower = None

    def setUp(self):
        #setup a data before every test case
        follower = FollowerFactory.create()

    def tearDown(self):
        #clean up data after every test cases
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    def createFollower(self, user='user_a', follower='user_b', chat_room="room1"):
        return Follower.objects.create(user=user, follower=follower, chat_room=chat_room)

    def test_followerModelCreation(self):
        #test objects creation of Model
        follower_object = self.createFollower()
        self.assertTrue(isinstance(follower_object, Follower))

    def test_userFieldMaxLength(self):
        #test a max_length of 'user' field
        follower = Follower.objects.get(id=1)
        max_length = follower._meta.get_field('user').max_length
        self.assertEqual(max_length, 200)

    def test_followerFieldMaxLength(self):
        #test a max_length of follower' field
        follower = Follower.objects.get(id=1)
        max_length = follower._meta.get_field('follower').max_length
        self.assertEqual(max_length, 200)

    def test_chatroomFieldMaxLength(self):
        #test a max_length of 'chat_room' field
        follower = Follower.objects.get(id=1)
        max_length = follower._meta.get_field('chat_room').max_length
        self.assertEqual(max_length, 100)

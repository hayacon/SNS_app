from django.test import TestCase
from .model_factories import *
from ..models import *

#test AppUSer model
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

    def create_AppUser(self, profileImage='abc.jpeg', dateOfBirth='1997-08-10', ocupation='teacher', organization='UoL', bio="hello world"):
        user = User.objects.create(username='user_a')
        return AppUser.objects.create(user=user, profileImage=profileImage, dateOfBirth=dateOfBirth, ocupation=ocupation, organization=organization,bio=bio)

    def test_appUserModelCreation(self):
        #test objects creation of Model
        appUserModel = self.create_AppUser()
        self.assertTrue(appUserModel, AppUser)

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


#test post model 
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

    def createPost(self, postId='10', postDate="2021-9-5", text="hello world", likes="300", media="/hello.jpeg"):
        user = User.objects.create(username="user_a")
        return Post.objects.create(postId=postId, user=user, postDate=postDate, text=text, likes=likes, media=media)

    def test_postModelCreation(self):
        #test objects creation of Model
        post_objects = self.createPost()
        self.assertTrue(isinstance(post_objects, Post))

    def test_testFieldMaxLength(self):
        #test max_length of 'text' field
        post = Post.objects.get(postId=5)
        max_length = post._meta.get_field('text').max_length
        self.assertEqual(max_length, 500)


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

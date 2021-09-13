import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .model_factories import *

#test UserList api
class userListApiTest(APITestCase):
    user = None
    good_url= None
    bad_url = None

    def setUp(self):
        self.user = UserFactory.create()
        self.good_url= reverse('user-list', kwargs={'username':"factory"})
        self.bad_url = 'api/user/1'

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test api with successful case
    def test_UserListResultOnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue("username" in data[0])

    #test api with situation where it should return 404
    def test_UserListResultFailOnBadId(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertTrue(response.status_code, 404)

#test PostList api
class postsListApiTest(APITestCase):
    posts = None
    good_url = None
    bad_url = None

    def setUp(self):
        self.posts = PostFactory.create()
        self.good_url = reverse('post', kwargs={'pk': 5})
        self.bad_url = "api/posts/abc"

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test api with successful case
    def test_PostsListOnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertTrue(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue("postId" in data[0])

    #test api with situation where it should return 404
    def test_PostsListOnFailWithBadId(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertTrue(response.status_code, 404)

#test NewPostList api
class newPostListApiTest(APITestCase):
    posts = None
    good_url = None
    bad_url = None

    def setUp(self):
        self.posts = PostFactory.create()
        self.good_url = reverse('new-post')
        self.bad_url = "api/post/12"

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test api with successful case
    def test_NewPostListOnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertTrue(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('postId' in data[0])

    #test api with situation where it should return 404
    def test_NewPostListOnBadUrl(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertTrue(response.status_code, 404)

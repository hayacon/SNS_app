from django.test import TestCase
from django.urls import reverse
from .model_factories import *
from ..views import *
import json

#test register view
class registerViewTest(TestCase):

    user = None
    profile = None

    def setUp(self):
        self.user = UserFactory.create()
        self.profile = AppUserFactory.create(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test post method
    def test_RegiserPostSuccess(self):
        data = {
            'username':'user',
            'password':'root',
            'email':'2@email.com',
            'first_name':'Goldsmith',
            'last_name':'uol',
            'dateOfBirth':'2000-10-10',
            'profileImage':'img.png',
            'ocupation':'Super hero',
            'organization':'avengers'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code , 200)

    #test a response of get
    def test_UrlExistATDesiredLocation(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    #test if view render correct template
    def test_RegisterUseCorrectTemplate(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snsApp/signup.html")

#test user_login view
class  userLoginViewTest(TestCase):

    user = None
    profile = None

    def setUp(self):
        self.user = UserFactory.create()
        self.profile = AppUserFactory.create(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test a response of get
    def test_UserLoginExistAtDesireLocation(self):
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code, 200)

    #test if view render correct template
    def test_UserLoginUseCorrctTemplate(self):
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'snsApp/login.html')

    def test_UserLoginPostSuccess(self):
        response = self.client.post(reverse('login'), {'username':'factory', 'password':'123'})
        self.assertEqual(response.status_code, 200)

#test user_logout view
class userLogOutViewTest(TestCase):

    #test a response of get
    def test_LogoutExistAtDesireLocation(self):
        response = self.client.get(reverse('logout'))
        self.assertTrue(response.status_code, 200)

    #test if view render correct template
    def test_LogoutUseCorrectTemplate(self):
        response = self.client.get(reverse('logout'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'snsApp/logout.html')

#test user_profile view
class userProfileViewTest(TestCase):

    user = None
    profile = None

    def setUp(self):
        self.user = UserFactory.create()
        self.profile = AppUserFactory.create(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test a response of get
    def test_UserProfileExistAtDesireLocation(self):
        response = self.client.get(reverse('user-profile'))
        self.assertTrue(response.status_code, 200)

    #not template test because ther is no template to be render in get

#test mian_user_home view
class mainUserHomeViewTest(TestCase):

    user = None
    profile = None

    def setUp(self):
        self.user = UserFactory.create()
        self.profile = AppUserFactory.create(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test a response of get
    def test_MainUserHomeExistAtDesireLocation(self):
        response = self.client.get(reverse('main-user-home'))
        self.assertTrue(response.status_code, 200)

#test user_home view
class userHomeViewTest(TestCase):

    user = None
    profile = None

    def setUp(self):
        self.user = UserFactory.create()
        self.profile = AppUserFactory.create(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        AppUser.objects.all().delete()
        Post.objects.all().delete()
        Follower.objects.all().delete()
        UserFactory.reset_sequence()
        AppUserFactory.reset_sequence()
        PostFactory.reset_sequence()
        FollowerFactory.reset_sequence()

    #test a response of get
    def test_UserHomeExistAtDesireLocation(self):
        response = self.client.get(reverse('user-home', kwargs={'username':'factory'}))
        self.assertTrue(response.status_code, 200)

#test user_search view
class userSearchViewTest(TestCase):

    #test a response of get
    def test_UserSearchExistAtDesireLocation(self):
        response = self.client.get(reverse('search-user'))
        self.assertTrue(response.status_code, 200)

    #not template test because ther is no template to be render in get

#test network_list view
class networkListViewTest(TestCase):

    #test a response of get
    def test_NetworkListExistAtDesireLocation(self):
        response = self.client.get(reverse('network-list'))
        self.assertTrue(response.status_code, 200)

#test post view
class postViewTest(TestCase):

    #test a response of get
    def test_PostViewExistAtDesireLocation(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code, 200)

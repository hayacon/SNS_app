from django.test import TestCase
from django.urls import reverse
from .model_factories import *
from ..views import *
import json


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

    def test_UrlExistATDesiredLocation(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_RegisterUseCorrectTemplate(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snsApp/signup.html")

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

    def test_UserLoginExistAtDesireLocation(self):
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code, 200)

    def test_UserLoginUseCorrctTemplate(self):
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'snsApp/login.html')

    def test_UserLoginPostSuccess(self):
        response = self.client.post(reverse('login'), {'username':'factory', 'password':'123'})
        self.assertEqual(response.status_code, 200)

class userLogOutViewTest(TestCase):

    def test_LogoutExistAtDesireLocation(self):
        response = self.client.get(reverse('logout'))
        self.assertTrue(response.status_code, 200)

    def test_LogoutUseCorrectTemplate(self):
        response = self.client.get(reverse('logout'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'snsApp/logout.html')

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

    def test_UserProfileExistAtDesireLocation(self):
        response = self.client.get(reverse('user-profile'))
        self.assertTrue(response.status_code, 200)

    #not template test because ther is no template to be render in get

    def test_UserProfilePostNoChanges(self):
        response = self.client.post(reverse('user-profile'))
        self.assertEqual(response.status_code, 302)

    def test_UserProfilePostPartialChanges(self):
        response = self.client.post(reverse('user-profile'), {'ocupation':'CEO', 'organization':'Google'})
        self.assertEqual(response.status_code, 302)

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

    def test_MainUserHomeExistAtDesireLocation(self):
        response = self.client.get(reverse('main-user-home'))
        self.assertTrue(response.status_code, 200)

    # def test_MainUserHomePostSuccess(self):
    #     response = self.client.post(reverse('main-user-home'), {'text':'hello there'})
    #     self.assertEqual(response.status_code, 200)

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

    def test_UserHomeExistAtDesireLocation(self):
        response = self.client.get(reverse('user-home', kwargs={'username':'factory'}))
        self.assertTrue(response.status_code, 200)

class userSearchViewTest(TestCase):

    def test_UserSearchExistAtDesireLocation(self):
        response = self.client.get(reverse('search-user'))
        self.assertTrue(response.status_code, 200)

    #not template test because ther is no template to be render in get
class networkListViewTest(TestCase):

    def test_NetworkListExistAtDesireLocation(self):
        response = self.client.get(reverse('network-list'))
        self.assertTrue(response.status_code, 200)

class postViewTest(TestCase):

    def test_PostViewExistAtDesireLocation(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code, 200)

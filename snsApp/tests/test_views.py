from django.test import TestCase
from django.urls import reverse
from .model_factories import *
from ..views import *

class registerViewTest(TestCase):

    def test_UrlExistATDesiredLocation(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_RegisterUseCorrectTemplate(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snsApp/signup.html")

class  userLoginViewTest(TestCase):

    def test_UserLoginExistAtDesireLocation(self):
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code, 200)

    def test_UserLoginUseCorrctTemplate(self):
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'snsApp/login.html')

class userLogOutViewTest(TestCase):

    def test_LogoutExistAtDesireLocation(self):
        response = self.client.get(reverse('logout'))
        self.assertTrue(response.status_code, 200)

    def test_LogoutUseCorrectTemplate(self):
        response = self.client.get(reverse('logout'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'snsApp/logout.html')

class userProfileViewTest(TestCase):

    def test_UserProfileExistAtDesireLocation(self):
        response = self.client.get(reverse('user-profile'))
        self.assertTrue(response.status_code, 200)

        #not template test because ther is no template to be render in get

class mainUserHomeViewTest(TestCase):

    def test_MainUserHomeExistAtDesireLocation(self):
        response = self.client.get(reverse('main-user-home'))
        self.assertTrue(response.status_code, 200)

    # def test_MainUserHomeUseCorrectTemplate(self):
    #     response = self.client.get(reverse('main-user-home'))
    #     self.assertTrue(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'snsApp/user_home.html')

#api test ?
class userHomeViewTest(TestCase):
    pass

class userSearchViewTest(TestCase):

    def test_UserSearchExistAtDesireLocation(self):
        response = self.client.get(reverse('search-user'))
        self.assertTrue(response.status_code, 200)

    #not template test because ther is no template to be render in get
class networkListViewTest(TestCase):

    def test_NetworkListExistAtDesireLocation(self):
        response = self.client.get(reverse('network-list'))
        self.assertTrue(response.status_code, 200)

#api test?
class postViewTest(TestCase):

    def test_PostViewExistAtDesireLocation(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code, 200)

class chatRoomViewTest(TestCase):

    def test_ChatRoomExistAtDesireLocation(self):
        response = self.client.get(reverse('chat-room', kwargs={'room_name':'room'}))
        self.assertTrue(response.status_code, 200)

    def test_ChatRoomUseCorrectTemplate(self):
        response = self.client.get(reverse('chat-room', kwargs={'room_name':'room'}))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'snsApp/chat_room.html')

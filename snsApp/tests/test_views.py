from django.test import TestCase
from django.urls import reverse
from .model_factories import *
from ..views import *

class registerViewTest(TestCase):
    #
    # def testUrlExistATDesiredLocation(self):
    #     response = self.client.get('/signup')
    #     self.assertEqual(response.status_code, 200)
    pass

class  userLoginViewTest(TestCase):
    pass

class userLogOutViewTest(TestCase):
    pass

class userProfileViewTest(TestCase):
    pass

class mainUserHomeViewTest(TestCase):
    pass

#api test ?
class userHomeViewTest(TestCase):
    pass

class userSearchViewTest(TestCase):
    pass

class networkListViewTest(TestCase):

    # def testGet(self):
    #     response = self.client.post('/friend_list')
    #     # self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "snsApp/network.html")
    pass
#api test?
class postViewTest(TestCase):
    pass

class chatRoomViewTest(TestCase):
    pass

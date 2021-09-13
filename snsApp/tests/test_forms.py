from django.test import TestCase
from .model_factories import *
from ..forms import *
from datetime import datetime

#test user form
class userFormTest(TestCase):
    #test label of each field
    def testUsernameFieldLabel(self):
        form = UserForm()
        self.assertTrue(form.fields['username'].label is '')

    def testpasswordFieldLabel(self):
        form = UserForm()
        self.assertTrue(form.fields['password'].label is '')

    def testEmailFieldLabel(self):
        form = UserForm()
        self.assertTrue(form.fields['email'].label is '')

    def testFirastNameFieldLabel(self):
        form = UserForm()
        self.assertTrue(form.fields['first_name'].label is '')

    def testLastNameFieldLabel(self):
        form = UserForm()
        self.assertTrue(form.fields['last_name'].label is '')

    #test form with some data
    def testUserForm(self):
        data = {'username':"user-a", "password":"123", "email":"user@example.com", "first_name":"John", "last_name":"A"}
        form = UserForm(data=data)
        self.assertTrue(form.is_valid)

    #test with invalid input
    def testUserFormWrongEmail(self):
        data = {'username':"user-a", "password":"123", "email":"user", "first_name":"John", "last_name":"A"}
        form = UserForm(data=data)
        self.assertEqual(form.is_valid(), False)

#test user profile form
class userProfileFormTest(TestCase):
    #test labels of each fields
    def testDateOfBirthFieldLabel(self):
        form = UserProfileForm()
        self.assertTrue(form.fields['dateOfBirth'].label == 'date of birth')

    def testOcupationFieldLabel(self):
        form = UserProfileForm()
        self.assertTrue(form.fields['ocupation'].label is '')

    def testOrganizationhFieldLabel(self):
        form = UserProfileForm()
        self.assertTrue(form.fields['organization'].label is '')

    def testprofileImageFieldLabel(self):
        form = UserProfileForm()
        self.assertTrue(form.fields['profileImage'].label == 'profile image')

    #test a form with data
    #test case 1
    def testUserProfileFormWithData(self):
        data = {'dateOfBirth':'08/21/1980', 'ocupation':'president', 'organization':'U.S.A', 'profileImage':'image.jpeg'}
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())

    #test case 2
    def testDateOfBirthFieldWithInvalidData(self):
        data = data = {'dateOfBirth':'August 1st 2000', 'ocupation':'president', 'organization':'U.S.A', 'profileImage':'image.jpeg'}
        form = UserProfileForm(data=data)
        self.assertEqual(form.is_valid(), False)

    #test case 3
    def testWithMinimalData(self):
        data = {'dateOfBirth':'08/21/1980'}
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())

#test userFormUpdate form
class userFormUpdateFormTest(TestCase):
    #test labels of each fields
    def testEmailFieldLabel(self):
        form = UserFormUpdate()
        self.assertTrue(form.fields['email'].label == 'email:')

    def testFirstNameFieldLabel(self):
        form = UserFormUpdate()
        self.assertTrue(form.fields['first_name'].label == 'first name')

    def testLastNameFieldLabel(self):
        form = UserFormUpdate()
        self.assertTrue(form.fields['last_name'].label == 'last name')

    #test form witrh data
    #test with passing no data
    def testWithEmptyData(self):
        data = {'emmail':None, 'first_name':None, 'last_name':None}
        form = UserFormUpdate(data=data)
        self.assertTrue(form.is_valid())

    #test with passing invalid email
    def testWithWrongEmail(self):
        data = {'email':'yo yo', 'first_name':'Donald', 'last_name':'McDonald'}
        form = UserFormUpdate(data=data)
        self.assertEqual(form.is_valid(), False)

#test userProfileUpdate form
class userProfileFormUpdateFormTest(TestCase):

    #test label of each feilds
    def testOcupationFieldLabel(self):
        form = UserProfileFormUpdate()
        self.assertTrue(form.fields['ocupation'].label == 'ocupation')

    def testOrganizationhFieldLabel(self):
        form = UserProfileFormUpdate()
        self.assertTrue(form.fields['organization'].label == 'organization')

    def testBioFieldLabel(self):
        form = UserProfileFormUpdate()
        self.assertTrue(form.fields['bio'].label == 'bio')

    def testprofileImageFieldLabel(self):
        form = UserProfileFormUpdate()
        self.assertTrue(form.fields['profileImage'].label == 'profile image')

    #test form with data
    #test with passing no data
    def testWithEmptyData(self):
        data = {'ocupation':None, 'organization':None, 'bio':None, 'profileImage':None}
        form = UserProfileFormUpdate(data=data)
        self.assertTrue(form.is_valid())

    #test with correct data
    def testWithEmptyData(self):
        data = {'ocupation':'CEO', 'organization':'Google', 'bio':'I love Apple', 'profileImage':'image.jpeg'}
        form = UserProfileFormUpdate(data=data)
        self.assertTrue(form.is_valid())

#test newPost form
class newPostFormTest(TestCase):

    #test label/help_text of each field
    def testTextFieldLabel(self):
        form = NewPostForm()
        self.assertTrue(form.fields['text'].label is '')

    def testTextFieldHelpText(self):
        form = NewPostForm()
        self.assertTrue(form.fields['text'].help_text == 'word limit : 500')

    def testMediaFieldLabel(self):
        form = NewPostForm()
        self.assertTrue(form.fields['media'].label == 'image')

    def testUserFieldLabel(self):
        form = NewPostForm()
        self.assertTrue(form.fields['user'].label is None)

    #test form with data
    #passing no data
    def testWithEmptyData(self):
        data = {'text':None, 'media':None, 'user':None}
        form = NewPostForm(data=data)
        self.assertEqual(form.is_valid(), False)

    #test with good data
    def testWithEmptyData(self):
        data = {'text':'hello world', 'media':'text.txt', 'user':None}
        form = NewPostForm(data=data)
        self.assertTrue(form.is_valid())

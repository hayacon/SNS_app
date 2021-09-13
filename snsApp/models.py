from django.db import models
from django.contrib.auth.models import User

# model for application user which is extended from django user model
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profileImage = models.ImageField(upload_to='images_profile', null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    ocupation = models.CharField(max_length=60, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

# model for each post
class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    postDate = models.DateField(null=True)
    text = models.CharField(max_length=500)
    likes = models.IntegerField(null=True)
    media = models.ImageField(upload_to='images_post')

#model for relationship between users
class Follower(models.Model):
    user = models.CharField(max_length=200)
    follower = models.CharField(max_length=200)
    chat_room = models.CharField(max_length=100, null=True)

from django.db import models
from django.contrib.auth.models import User

# model for application user which is extended from django user model
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creationDate = models.DateField(null=False)
    profileImage = models.ImageField(upload_to='images_profile', null=False, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

# model for each post
class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    postDate = models.DateField()
    text = models.CharField(max_length=500)
    likes = models.IntegerField()
    media = models.ImageField(upload_to='images_post')

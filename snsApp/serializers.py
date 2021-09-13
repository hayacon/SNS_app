from rest_framework import serializers
from .models import *

#serializer of AppUser model
class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['profileImage', 'dateOfBirth', 'ocupation', 'organization', 'bio']

#serializer for post model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postId', 'user', 'postDate', 'text', 'media', 'likes']

#serializer combining user model, appuser model and post model
class UserSerializer(serializers.ModelSerializer):
    profile = AppUserSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','profile','posts']

#serializer for follower model
class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follower
        fields=['user', 'follower', 'chat_room']

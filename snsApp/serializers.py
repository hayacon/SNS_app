from rest_framework import serializers
from .models import *

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['profileImage', 'dateOfBirth', 'ocupation', 'organization', 'bio']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postId', 'user', 'postDate', 'text', 'media', 'likes']

class UserSerializer(serializers.ModelSerializer):
    profile = AppUserSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','profile','posts']

class UserPostSerialzer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model=User
        fields = ['username', 'posts']

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follower
        fields=['user', 'follower', 'chat_room']

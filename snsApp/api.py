from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins

#api for specofic user, specify by username
class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        user = User.objects.filter(username=username)
        return user

#api for a spcific post specified by postId
class PostsList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        postId = self.kwargs['pk']
        return Post.objects.filter(postId=postId)

#api for all post
class NewPostList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

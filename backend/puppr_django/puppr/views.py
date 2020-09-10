from rest_framework import generics
from django.shortcuts import render
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from django.http import HttpResponse
import random
import json

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# POSSIBLE REACT ROUTING
# def index(request):
#     template = loader.get_template('puppr/index.html')

#     return HttpResponse(template.render())

# def api (request):
#     if request.method == 'POST':
#         query = json.loads(request.GET[''])

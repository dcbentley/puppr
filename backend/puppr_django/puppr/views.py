from rest_framework.generic import ListAPIView, RetrieveAPIView
from django.shortcuts import render
from .models import User, UserPost
from .serializers import UserSerializer

# Create your views here.

class UserListView(ListAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer

# def user_post(request):
#     user_post = UserPost.objects.all()
#     return render(request, '')

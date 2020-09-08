from django.shortcuts import render
from .models import User, UserPost

# Create your views here.

def user_post(request):
    user_post = UserPost.objects.all()
    return render(request, '')
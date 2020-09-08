from rest_framework import serializers
from .models import User, UserPost

class UserSerializer(serializers.ModelsSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'pup_name', 'profile_img_url')
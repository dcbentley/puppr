from rest_framework import serializers
from .models import User, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True,
    )
    user_url = serializers.ModelSerializer.serializer_url_field(view_name='user_detail')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'pup_name', 'profile_img_url', 'posts', 'user_url')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True,
    )


    user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    source='user'
    )
    class Meta:
        model = Post
        fields = ('id', 'user', 'post', 'user_id')

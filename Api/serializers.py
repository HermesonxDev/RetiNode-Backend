from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DiscussionSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, source='user.name')

    class Meta:
        model = Discussions
        fields = ('postID', 'user_name', 'linkPost', 'date', 'title', 'description', 'image', 'likes', 'reads')

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=255, min_length=None, allow_blank=False, trim_whitespace=True, source='user.name')

    class Meta:
        model = Comments
        fields = ('commentID', 'user_name', 'text', 'date', 'commented_post', 'likes')
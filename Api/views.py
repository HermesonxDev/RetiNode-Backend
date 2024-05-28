from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET'])
def discussions(request):
    discussions = Discussions.objects.all()
    serialized_discussions = DiscussionSerializer(discussions, many=True)
    if discussions:
        return Response(serialized_discussions.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_discussion(request):
    if request.method == "GET":
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        user = request.data.get('user_name')
        user_name = User.objects.get(name=user)
        link_profile = request.data.get('linkPost')
        title = request.data.get('title')
        description = request.data.get('description')
        image = request.data.get('image')

        if user_name:
            create_discussion = Discussions.objects.create(user=user_name, linkPost=link_profile, title=title, description=description, image=image)
            create_discussion.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    if users:
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def logs(request):
    logs = Logs.objects.all()
    serialized_logs = LogsSerializer(logs, many=True)
    if logs:
        return Response(serialized_logs.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def lastLog(request):
    log = Logs.objects.first()
    serialized_log = LogsSerializer(log)
    if log:
        return Response(serialized_log.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def trendingArticles(request):
    articles = Discussions.objects.filter(reads__gte=500)
    serialized_articles = DiscussionSerializer(articles, many=True)
    if articles:
        return Response(serialized_articles.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def comments(request):
    comments = Comments.objects.all()
    serialized_comment = CommentSerializer(comments, many=True)
    if comments:
        return Response(serialized_comment.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def commentators_of_the_week(request):
    commentators = Comments.objects.filter(likes__gte=500)
    serialized_commentators = CommentSerializer(commentators, many=True)
    if commentators:
        return Response(serialized_commentators.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
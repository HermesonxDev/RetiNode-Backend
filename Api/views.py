from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import *
from .serializers import *


class DiscussionViewSet(ModelViewSet):
    queryset = Discussions.objects.all()
    serializer_class = DiscussionSerializer

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def get_discussions(self, request):
        try:
            discussions = self.queryset
            serializer = self.serializer_class(discussions, many=True)
            if discussions:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return {'message': 'Ocorreu um erro ao listar as discussões.', 'error': str(error)}
        
    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def create_discussion(self, request):
        try:
            if request.method == "GET":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                user = request.data.get('user_name')
                link_profile = request.data.get('linkPost')
                title = request.data.get('title')
                description = request.data.get('description')
                image = request.data.get('image')

                user_name = User.objects.get(name=user)

                if user_name:
                    create_discussion = Discussions.objects.create(user=user_name, linkPost=link_profile, title=title, description=description, image=image)
                    create_discussion.save()
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return {'message': 'Ocorreu um erro na criação de uma nova discussão', 'error': str(error)}

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def get_users(self, request):
        try:
            users = self.queryset
            serializer = self.serializer_class(users, many=True)
            if users:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return {'message': 'Ocorreu um erro na aplicação', 'error': str(error)}

# @api_view(['GET'])
# def logs(request):
#     try:
#         logs = Logs.objects.all()
#         serialized_logs = LogsSerializer(logs, many=True)
#         if logs:
#             return Response(serialized_logs.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     except Exception as error:
#         return {'message': 'Ocorreu um erro na aplicação', 'error': str(error)}

# @api_view(['GET'])
# def lastLog(request):
#     try:
#         log = Logs.objects.first()
#         serialized_log = LogsSerializer(log)
#         if log:
#             return Response(serialized_log.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     except Exception as error:
#         return {'message': 'Ocorreu um erro na aplicação', 'error': str(error)}

# @api_view(['GET'])
# def trendingArticles(request):
#     try:
#         articles = Discussions.objects.filter(reads__gte=500)
#         serialized_articles = DiscussionSerializer(articles, many=True)
#         if articles:
#             return Response(serialized_articles.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     except Exception as error:
#         return {'message': 'Ocorreu um erro na aplicação', 'error': str(error)}

# @api_view(['GET'])
# def comments(request):
#     try:
#         comments = Comments.objects.all()
#         serialized_comment = CommentSerializer(comments, many=True)
#         if comments:
#             return Response(serialized_comment.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     except Exception as error:
#         return {'message': 'Ocorreu um erro na aplicação', 'error': str(error)}

# @api_view(['GET'])
# def commentators_of_the_week(request):
#     try:
#         commentators = Comments.objects.filter(likes__gte=500)
#         serialized_commentators = CommentSerializer(commentators, many=True)
#         if commentators:
#             return Response(serialized_commentators.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     except Exception as error:
#         return {'message': 'Ocorreu um erro na aplicação', 'error': str(error)}
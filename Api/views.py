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
            return {'message': 'Ocorreu um erro ao listar os usuários', 'error': str(error)}

class LogViewSet(ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def get_logs(self, request):
        try:
            logs = self.queryset
            serializer = self.serializer_class(logs, many=True)
            if logs:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return {'message': 'Ocorreu um erro ao listar os logs', 'error': str(error)}

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def last_log(self, request):
        try:
            log = Logs.objects.first()
            serializer = self.serializer_class(log)
            if log:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return {'message': 'Ocorreu um erro ao buscar o último log', 'error': str(error)}

class TrendingArticlesViewSet(ModelViewSet):
    queryset = Discussions.objects.all()
    serializer_class = DiscussionSerializer

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def get_trendingArticles(self, request):
        try:
            articles = Discussions.objects.filter(reads__gte=500)
            serializer = self.serializer_class(articles, many=True)
            if articles:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return {'message': 'Ocorreu um erro ao listar os artigos em alta', 'error': str(error)}

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def get_comments(self, request):
        try:
            comments = self.queryset
            serializer = self.serializer_class(comments, many=True)
            if comments:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return {'message': 'Ocorreu um erro ao listar os comentários', 'error': str(error)}

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def commentators_of_the_week(self, request):
        try:
            commentators = Comments.objects.filter(likes__gte=500)
            serializer = self.serializer_class(commentators, many=True)
            if commentators:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return {'message': 'Ocorreu um erro ao listar os comentaristas da semana', 'error': str(error)}
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import *
from .serializers import *

class AuthenticationViewSet(ModelViewSet):
    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def signUp(request):
        try:
            if request.method == "GET":
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                name = request.data.get("name")
                username = request.data.get("username")
                date_of_birth = request.data.get("")
                email = request.data.get("email")
                password = request.data.get("password")

                new_user = User.objects.create(name=name, username=username, date_of_birth=date_of_birth, email=email)
                new_user.save()

                return Response("Usuário cadastrado com sucesso!", status=status.HTTP_200_OK)
        except Exception as error:
            return {'message': f'Ocorreu um ao erro tentar cadastrar o usuário {username}.'}


    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def login(request):
        try:
            if request.method == "GET":
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                username = request.data.get("username")
                password = request.data.get("password")

                user = authenticate(username=username, password=password)

                if user:
                    login_django(request, user)
                    return Response("Usuário logado com sucesso!", status=status.HTTP_200_OK)
                else:
                    return Response("Usuário ou/e senha incorretos", status=status.HTTP_403_FORBIDDEN)
        except Exception as error:
            return {'message': f'Ocorreu um erro ao tentar logar com o usuário {username}.', 'error': str(error)}


    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def logout(request):
        try:
            logout_django(request)
            return Response("Usuário deslogado com sucesso!", status=status.HTTP_200_OK)
        except Exception as error:
            return {'message': f'Ocorreu um erro ao tentar deslogar o usuário.'}


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
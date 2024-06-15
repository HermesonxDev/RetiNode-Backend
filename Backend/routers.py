from rest_framework import routers

from Api.views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'discussions', DiscussionViewSet, basename='discussions')
router.register(r'users', UserViewSet, basename='users')
router.register(r'logs', LogViewSet, basename='logs')
router.register(r'trending_articles', TrendingArticlesViewSet, basename='trending_articles')
router.register(r'comments', CommentsViewSet, basename='comments')
router.register(r'authenticate', AuthenticationViewSet, basename='authenticate')
from rest_framework import routers

from Api.views import DiscussionViewSet, UserViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'discussions', DiscussionViewSet, basename='discussions')
router.register(r'users', UserViewSet, basename='users')
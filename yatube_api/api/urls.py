from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register('v1/follow', FollowViewSet, basename='comment')
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import (PostViewSet, CommentViewSet,
                    GroupViewSet, FollowViewSet)


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follows')

post_router = NestedSimpleRouter(router, 'posts', lookup='post')
post_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls + post_router.urls))
]

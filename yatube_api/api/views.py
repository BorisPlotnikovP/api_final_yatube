from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Follow, Group, Post
from .mixins import (ListCreateViewSet, ListRetrieveViewSet,
                     DefaultPermissionMixin)
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)


class PostViewSet(DefaultPermissionMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group', 'author')
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(DefaultPermissionMixin):
    serializer_class = CommentSerializer

    def get_post_pk(self):
        return self.kwargs.get('post_pk')

    def get_queryset(self):
        return Comment.objects.all().filter(post=self.get_post_pk())

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.get_post_pk())
        author = self.request.user
        serializer.save(post=post, author=author)


class GroupViewSet(ListRetrieveViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Follow.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

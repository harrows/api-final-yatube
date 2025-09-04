from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from posts.models import Group, Post

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author", "group").all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_post(self):
        if not hasattr(self, "_post"):
            self._post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return self._post

    def get_queryset(self):
        return self.get_post().comments.select_related("author")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ("=following__username",)

    def get_queryset(self):
        return self.request.user.follower.select_related("user", "following")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

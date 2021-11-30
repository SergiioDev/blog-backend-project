from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from src.blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class PostUserWritePermission(BasePermission):
    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

        # Define Custom QuerySet
    def get_queryset(self):
        return Post.objects.all()

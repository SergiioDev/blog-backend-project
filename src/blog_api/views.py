from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from src.blog.models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions


class PostList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer

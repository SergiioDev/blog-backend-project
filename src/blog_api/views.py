from rest_framework import generics, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from src.blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions


# class PostUserWritePermission(BasePermission):
#   message = "Editing posts is restricted to the author only."

#  def has_object_permission(self, request, view, obj):
#     if request.method in SAFE_METHODS:
#        return True

#   return obj.author == request.user

class PostList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


# class CreatePost(generics.CreateAPIView):
#    permission_classes = [IsAuthenticated]
#    queryset = Post.post_objects.all()
#    serializer_class = PostSerializer
class CreatePost(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        print(request.data)
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer

# Easy form
# class PostList(viewsets.ViewSet):
#  permission_classes = [IsAuthenticated]
#  queryset = Post.post_objects.all()

# def list(self, request):
#    serializer = PostSerializer(self.queryset, many=True)
#   return Response(serializer.data)

# def retrieve(self, request, pk=None):
#    post = get_object_or_404(self.queryset, pk=pk)
#   serializer = PostSerializer(post)
#   return Response(serializer.data)

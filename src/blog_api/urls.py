from django.urls import path

from src.blog_api.views import PostList, PostDetail, CreatePost, DeletePost, EditPost

app_name = 'src.blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('create/', CreatePost.as_view(), name='createpost'),
    path('edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]

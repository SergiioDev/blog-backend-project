from django.urls import path
from src.blog_api.views import PostList, PostDetail

app_name = 'src.blog_api'

urlpatterns = [
    path('<int:pk>', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
]

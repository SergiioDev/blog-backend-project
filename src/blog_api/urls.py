from src.blog_api.views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'src.blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls

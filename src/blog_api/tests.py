from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from src.blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        """
        Ensure we can create a new Post object and view object.
        """
        self.test_category = Category.objects.create(name='django')

        db = get_user_model()

        super_user = db.objects.create_superuser(
            'testuser@super.com', 'username', 'firstname', 'password'
        )

        self.client.login(username=super_user.email,
                          password='password')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')

        # TODO change this wen we have a token
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_update(self):

        client = APIClient()

        db = get_user_model()
        user = db.objects.create_user(
            'testuser@user.com', 'username', 'firstname', 'password'
        )

        self.test_category = Category.objects.create(name='django')

        test_post = Post.objects.create(
            category_id=1, title='Post Title',
            excerpt='Post Excerpt', content='Post Content',
            slug='post-title', author_id=1, status='published')

        client.login(username=user.email,
                     password='123456789')

        url = reverse('blog_api:detailcreate', kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json')

        print(response.data)

        # TODO change this wen we have a token
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_update_permissions(self):

        client = APIClient()

        db = get_user_model()
        user = db.objects.create_user(
            'testuser@user.com', 'username', 'firstname', 'password'
        )

        user2 = db.objects.create_user(
            'testuser2@user.com', 'usernamee', 'firstname', 'password'
        )

        self.test_category = Category.objects.create(name='django')

        test_post = Post.objects.create(
            category_id=1, title='Post Title',
            excerpt='Post Excerpt', content='Post Content',
            slug='post-title', author_id=1, status='published')

        client.login(username=user2.email,
                     password='password')

        url = reverse('blog_api:detailcreate', kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json')

        # TODO change this wen we have a token
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

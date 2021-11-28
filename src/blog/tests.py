from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post


class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user = User.objects.create(username='test_user', password='123456789')
        test_post = Post.objects.create(
            category_id=1,
            title='Post Title',
            excerpt='Post Excerpt',
            content='Post Content',
            slug='post-title',
            author_id=1,
            status='published',
        )

    def test_blog_content(self):
        post = Post.post_objects.get(id=1)
        category = Category.objects.get(id=1)

        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(author, 'test_user')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(category), "django")

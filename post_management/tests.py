from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            content='Test Content',
            video_url='http://example.com/video',
            image='path/to/image.jpg',
            social_media_accounts={'facebook': 'fb_account'},
            user=self.user
        )

    def test_post_creation(self):
        self.assertEqual(str(self.post), f"Post by {self.user.username} at {self.post.created_at}")

class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.post = Post.objects.create(
            content='Test Content',
            video_url='http://example.com/video',
            image='path/to/image.jpg',
            social_media_accounts={'facebook': 'fb_account'},
            user=self.user
        )

    def test_create_post_view(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_new_post.html')

    def test_list_post_view(self):
        response = self.client.get(reverse('list_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_posts.html')
        self.assertContains(response, 'Test Content')

    def test_detail_post_view(self):
        response = self.client.get(reverse('detail_post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_post.html')
        self.assertContains(response, 'Test Content')

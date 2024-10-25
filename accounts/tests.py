from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class UserTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_signup_view(self):
        response = self.client.post(reverse('signup'), {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'confirm_password': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects after signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        })
        self.assertEqual(response.status_code, 302)  # Redirects after login
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)

    def test_profile_view(self):
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user_data['username'])

    def test_edit_profile_view(self):
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        response = self.client.post(reverse('edit_profile'), {
            'username': 'updateduser',
            'first_name': 'Updated',
            'last_name': 'User',
        })
        self.assertEqual(response.status_code, 302)  # Redirects after update
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'User')

class PostTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post_data = {
            'content': 'Test content',
            'video_url': 'http://example.com/video',
            'social_media_accounts': {'twitter': 'test'},
            'user': self.user
        }
        self.client.login(username='testuser', password='password123')

    def test_create_post_view(self):
        response = self.client.post(reverse('create_post'), {
            'content': self.post_data['content'],
            'video_url': self.post_data['video_url'],
            'social_media_accounts': self.post_data['social_media_accounts'],
        })
        self.assertEqual(response.status_code, 302)  # Redirects after creation
        self.assertTrue(Post.objects.filter(content='Test content').exists())

    def test_list_post_view(self):
        Post.objects.create(**self.post_data)
        response = self.client.get(reverse('list_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test content')

    def test_detail_post_view(self):
        post = Post.objects.create(**self.post_data)
        response = self.client.get(reverse('detail_post', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test content')

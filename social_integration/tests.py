from django.test import TestCase
from django.contrib.auth.models import User
from post_management.models import Post  # Assuming this exists
from accounts.models import SocialMediaAccount, SocialMediaPost, UserProfile  # Import your models

class SocialMediaAccountTest(TestCase):

    def setUp(self):
        # Create a User for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_social_media_account_creation(self):
        account = SocialMediaAccount.objects.create(
            user=self.user,
            platform_name='Twitter',
            full_name='Test User',
            access_token='test_access_token',
            screen_name='testuser',
        )
        self.assertEqual(account.platform_name, 'Twitter')
        self.assertEqual(account.full_name, 'Test User')
        self.assertEqual(str(account), 'Test User - Twitter')

    def test_social_media_account_str_with_screen_name(self):
        account = SocialMediaAccount.objects.create(
            user=self.user,
            platform_name='LinkedIn',
            screen_name='test_screen_name',
            access_token='test_access_token',
        )
        self.assertEqual(str(account), 'test_screen_name - LinkedIn')


class SocialMediaPostTest(TestCase):

    def setUp(self):
        # Create a User, SocialMediaAccount, and Post for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.social_media_account = SocialMediaAccount.objects.create(
            user=self.user,
            platform_name='Twitter',
            access_token='test_access_token'
        )
        self.post = Post.objects.create(title='Test Post', content='This is a test post')

    def test_social_media_post_creation(self):
        social_post = SocialMediaPost.objects.create(
            post=self.post,
            social_media_account=self.social_media_account,
            post_status='Posted'
        )
        self.assertEqual(social_post.post_status, 'Posted')
        self.assertEqual(str(social_post), f"Post {self.post.id} on Twitter - Status: Posted")


class UserProfileTest(TestCase):

    def setUp(self):
        # Create a user and check if the profile is created automatically
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_profile_creation(self):
        # Check if the UserProfile is created by signals
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.user.username, 'testuser')

    def test_user_profile_str(self):
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(user_profile), 'testuser')

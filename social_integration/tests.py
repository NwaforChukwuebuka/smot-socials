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
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch, Mock
from social_django.models import UserSocialAuth
from accounts.models import SocialMediaAccount

class LinkedInPostViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    @patch('requests.post')
    def test_linkedin_post_success(self, mock_post):
        # Mock a successful LinkedIn API response
        mock_response = Mock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response

        # Create a mock linked LinkedIn account for the user
        UserSocialAuth.objects.create(
            user=self.user,
            provider='linkedin-oauth2',
            extra_data={'access_token': 'test_token', 'uid': 'test_uid'}
        )

        # Send a POST request with a message
        response = self.client.post(reverse('linkedin_post'), {'message': 'Test LinkedIn Post'})
        
        # Check that the request is redirected to the dashboard
        self.assertRedirects(response, reverse('dashboard'))

    @patch('requests.post')
    def test_linkedin_post_no_message(self, mock_post):
        response = self.client.post(reverse('linkedin_post'), {'message': ''})
        self.assertContains(response, 'Message cannot be empty')

    def test_linkedin_post_no_account(self):
        # Test when the user doesn't have a LinkedIn account linked
        response = self.client.post(reverse('linkedin_post'), {'message': 'Test LinkedIn Post'})
        self.assertContains(response, 'LinkedIn account not linked')

    @patch('requests.post')
    def test_linkedin_post_error(self, mock_post):
        # Mock a failed LinkedIn API response
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {'message': 'Invalid request'}
        mock_post.return_value = mock_response

        UserSocialAuth.objects.create(
            user=self.user,
            provider='linkedin-oauth2',
            extra_data={'access_token': 'test_token', 'uid': 'test_uid'}
        )

        response = self.client.post(reverse('linkedin_post'), {'message': 'Test LinkedIn Post'})
        self.assertContains(response, 'Unable to post to LinkedIn: Invalid request')


class UnlinkSocialAccountViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_unlink_social_account_success(self):
        # Create a mock social account
        social_account = UserSocialAuth.objects.create(user=self.user, provider='twitter')

        response = self.client.post(reverse('unlink_social_account', args=['twitter']))

        # Check that the social account has been unlinked (deleted)
        with self.assertRaises(UserSocialAuth.DoesNotExist):
            UserSocialAuth.objects.get(provider='twitter')

        # Check that the user is redirected to the dashboard
        self.assertRedirects(response, '/dashboard')

    def test_unlink_social_account_does_not_exist(self):
        response = self.client.post(reverse('unlink_social_account', args=['facebook']))
        self.assertContains(response, 'No linked account found for Facebook')


class TwitterConnectViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    @patch('tweepy.OAuth1UserHandler.get_authorization_url')
    def test_twitter_connect_success(self, mock_get_authorization_url):
        # Mock the redirect URL for Twitter OAuth
        mock_get_authorization_url.return_value = 'http://twitter.com/auth'

        response = self.client.get(reverse('twitter_connect'))

        # Check that the user is redirected to Twitter's OAuth page
        self.assertRedirects(response, 'http://twitter.com/auth')

    @patch('tweepy.OAuth1UserHandler.get_authorization_url')
    def test_twitter_connect_error(self, mock_get_authorization_url):
        # Mock TweepError
        mock_get_authorization_url.side_effect = tweepy.TweepError

        response = self.client.get(reverse('twitter_connect'))
        self.assertRedirects(response, reverse('error_page'))


class TwitterCallbackViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.session = self.client.session
        self.session['request_token'] = {'oauth_token': 'test_token', 'oauth_token_secret': 'test_secret'}
        self.session.save()

    @patch('tweepy.OAuth1UserHandler.get_access_token')
    @patch('tweepy.API.verify_credentials')
    def test_twitter_callback_success(self, mock_verify_credentials, mock_get_access_token):
        # Mock Twitter access token and credentials
        mock_get_access_token.return_value = ('access_token', 'access_token_secret')
        mock_verify_credentials.return_value = Mock(screen_name='testuser', profile_image_url_https='http://image.url')

        response = self.client.get(reverse('twitter_callback'), {'oauth_verifier': 'test_verifier'})

        # Check that the user's social media account is created
        self.assertTrue(SocialMediaAccount.objects.filter(user=self.user, platform_name='Twitter').exists())

        # Check that the user is redirected to the dashboard
        self.assertRedirects(response, reverse('dashboard'))

    @patch('tweepy.OAuth1UserHandler.get_access_token')
    def test_twitter_callback_error(self, mock_get_access_token):
        mock_get_access_token.side_effect = tweepy.TweepError

        response = self.client.get(reverse('twitter_callback'), {'oauth_verifier': 'test_verifier'})
        self.assertRedirects(response, reverse('error_page'))


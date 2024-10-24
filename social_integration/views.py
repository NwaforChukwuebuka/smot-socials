from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from social_django.models import UserSocialAuth
import tweepy
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
import logging
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


class UserConnectionsView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure token-based authentication is used

    def get(self, request):
        """
        Retrieve the user's social connections status.
        """
        twitter_connected = UserSocialAuth.objects.filter(user=request.user, provider='twitter').exists()
        facebook_connected = UserSocialAuth.objects.filter(user=request.user, provider='facebook').exists()
        instagram_connected = UserSocialAuth.objects.filter(user=request.user, provider='instagram').exists()

        return Response({
            'twitter': twitter_connected,
            'facebook': facebook_connected,
            'instagram': instagram_connected,
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_to_twitter(request):
    user = request.user
    media = request.FILES.get('media')  # Accepting media file only

    if not media:
        return Response({"error": "Media file is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Get Twitter credentials from user's social auth
        twitter_user = user.social_auth.get(provider='twitter')
        access_token_data = twitter_user.extra_data.get('access_token', {})
        access_token = access_token_data.get('oauth_token')
        access_token_secret = access_token_data.get('oauth_token_secret')

        # Authenticate with Twitter
        auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Use Tweepy's media_upload to post the media
        media_upload = api.media_upload(filename=media.name, file=media)

        # Post the tweet with the uploaded media
        api.update_status(status='', media_ids=[media_upload.media_id])  # Empty tweet content, media only

        return Response({"success": "Media posted successfully to Twitter."}, status=status.HTTP_200_OK)

    except KeyError:
        return Response({"error": "Twitter account not connected."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

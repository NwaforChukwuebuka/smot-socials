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
    tweet_content = request.data.get('tweet')

    if not tweet_content:
        return Response({"error": "Tweet content is required."}, status=status.HTTP_400_BAD_REQUEST)

    # Assuming you have a model that stores the social auth data
    try:
        # Assuming user has related model `social_auth` with stored tokens
        twitter_user = user.social_auth.get(provider='twitter')
        # Access the nested access_token dictionary
        access_token_data = twitter_user.extra_data.get('access_token', {})
        access_token = access_token_data.get('oauth_token')
        access_token_secret = access_token_data.get('oauth_token_secret')

        auth = tweepy.OAuthHandler(SOCIAL_AUTH_TWITTER_KEY,SOCIAL_AUTH_TWITTER_SECRET )  # Use your Twitter app credentials
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        
        # Post tweet using Tweepy
        api.update_status(status=tweet_content)
        return Response({"success": "Tweet posted successfully."}, status=status.HTTP_200_OK)
    except KeyError:
        return Response({"error": "Twitter account not connected."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

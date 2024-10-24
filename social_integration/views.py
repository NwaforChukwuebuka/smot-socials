from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse
from .models import SocialMediaAccount
from django.utils.decorators import method_decorator
import requests
from social_django.models import UserSocialAuth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
import tweepy
from django.conf import settings
from requests_oauthlib import OAuth1Session

def save_twitter_token(user, token):
    """Save Twitter access token for the user."""
    try:
        user_social_auth = user.social_auth.get(provider='twitter')
        user_social_auth.extra_data['access_token'] = token
        user_social_auth.save()  # Save the user social auth object with the new token
    except UserSocialAuth.DoesNotExist:
        # Handle the case where the user does not have a Twitter account linked
        pass

@login_required
def linkedin_post(request):
    if request.method == "POST":
        message = request.POST.get('message')
        print(message)
        
        if not message:
            # Handle empty message error by redirecting with an error message
            return render(request, 'dashboard.html', {'error': 'Message cannot be empty'})

        # Here, we assume the user has linked their LinkedIn account
        try:
            user_social_auth = request.user.social_auth.get(provider='linkedin-oauth2')
            access_token = user_social_auth.extra_data['access_token']
            uid = user_social_auth.extra_data['uid']  # Ensure uid is available
        except UserSocialAuth.DoesNotExist:
            # Handle case where the user hasn't linked their LinkedIn account
            return render(request, 'dashboard.html', {'error': 'LinkedIn account not linked'})

        # Check if the uid is valid
        if not uid:
            return render(request, 'dashboard.html', {'error': 'LinkedIn account is not properly linked. Please reconnect.'})

        # LinkedIn API endpoint for creating a post
        post_url = 'https://api.linkedin.com/v2/ugcPosts'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-Restli-Protocol-Version': '2.0.0',
            'Content-Type': 'application/json',
        }

        # Create the post body as per LinkedIn's API requirements
        post_data = {
            "author": f"urn:li:person:{uid}",  # Format the author field correctly
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": message  # Use the provided message
                    },
                    "shareMediaCategory": "NONE"  # Set to NONE for text-only post
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"  # Set visibility to public
            }
        }

        # Send the post request to LinkedIn
        response = requests.post(post_url, headers=headers, json=post_data)
        
        if response.status_code == 201:
            # Successful post creation
            messages.success(request, 'Post successfully created on LinkedIn!')
            return redirect('dashboard')  # Redirect to the dashboard or desired page
        else:
            # Handle LinkedIn API errors
            error_message = response.json().get('message', 'Unknown error occurred')
            return render(request, 'dashboard.html', {'error': f'Unable to post to LinkedIn: {error_message}'})

    return render(request, 'dashboard.html')
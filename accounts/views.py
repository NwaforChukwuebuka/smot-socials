from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.shortcuts import redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token


def token(request):
    # Your view logic here
    return render(request, 'token.html')
def authorize(request):
    # Handle Google OAuth2 authorization here
    return redirect('dashboard') 

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})

# Registration View
class RegisterView(APIView):
    """
    API view to handle user registration.
    """
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer  # Add this line

    def post(self, request, *args, **kwargs):
        print(request.data)  # Print the incoming data
        serializer = self.serializer_class(data=request.data)  # Now this works
        if serializer.is_valid():
            user = serializer.save(request)  # Save the user and get the user object
            user.refresh_from_db()  # Refresh the user instance from the database to ensure it's saved
            
            # Now create the token after the user is saved
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'user': UserProfileSerializer(user).data,
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# Login View
class LoginView(ObtainAuthToken):
    """
    API view to handle user login and token generation.
    """
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user login.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({
                'user': UserProfileSerializer(serializer.validated_data['user']).data,
                'token': serializer.validated_data['token']
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Profile View
class UserProfileView(APIView):
    """
    API view to retrieve the authenticated user's profile.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Handle GET request to retrieve the authenticated user's profile.
        """
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



# Logout View
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    API view to handle user logout by deleting the authentication token.
    """
    request.user.auth_token.delete()
    return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)




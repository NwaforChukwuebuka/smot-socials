from rest_framework import serializers
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

# Serializer for User Registration
class UserRegistrationSerializer(RegisterSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def validate(self, data):
        # Check if the username or email already exists
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError("Username already exists.")
        
        if User.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError("Email already exists.")
        
        # Ensure the passwords match
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()  # Ensure the user is saved

        # Return only the user
        return user

# Serializer for User Login
class UserLoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        username_or_email = data.get('username_or_email', None)
        password = data.get('password', None)

        if not username_or_email or not password:
            raise serializers.ValidationError('Both "username/email" and "password" are required.')

        User = get_user_model()
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid credentials. Please try again.')
        else:
            user = authenticate(username=username_or_email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid credentials. Please try again.')
        if not user.is_active:
            raise serializers.ValidationError('This user is inactive.')

        token, created = Token.objects.get_or_create(user=user)

        return {
            'user': user,
            'token': token.key,
        }

# Serializer for User Profile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

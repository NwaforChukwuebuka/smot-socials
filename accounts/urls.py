# from django.urls import path, include
# from .views import register_user

# urlpatterns = [
#     path('register/', register_user, name='register'),
#     path('auth/google/', GoogleLogin.as_view(), name='google-login'),
# ]


from django.urls import path, include
from .views import LoginView, RegisterView, logout_view, get_csrf_token, GoogleLogin, UserProfileView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api_login'),  # Custom LoginView
    path('api/register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('csrf/', get_csrf_token, name='csrf'),
    path('google/', GoogleLogin.as_view(), name='google_login'),  # Google OAuth route
    path('api/profile/', UserProfileView.as_view(), name='user_profile'),  # User profile route
    path('accounts/', include('allauth.urls')),  # Include allauth routes for social authentication
]


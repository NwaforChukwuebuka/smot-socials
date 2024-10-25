# from django.urls import path, include
# from .views import register_user

# urlpatterns = [
#     path('register/', register_user, name='register'),
#     path('auth/google/', GoogleLogin.as_view(), name='google-login'),
# ]

from django.urls import path
from .views import SignupView, LoginView, ProfileView, EditProfileView, logout_view

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),  # New URL
    path('logout/', logout_view, name='logout'),
]
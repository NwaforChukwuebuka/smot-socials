# smot/social_integration/urls.py

from django.urls import path
from .views import UserConnectionsView,post_to_twitter
# from .views import switch_account

urlpatterns = [
     path('api/user/connections/', UserConnectionsView.as_view(), name='user-connections'),
     path('api/twitter/post/', post_to_twitter, name='post_to_twitter'),
    # path('switch_account/<str:provider>/', switch_account, name='switch_account'),
    # # Other URL patterns can be added here...
]


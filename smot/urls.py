from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.views.generic import TemplateView
from dashboard.views import dashboard_view
from core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    # allauth URLs
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),

    # dj-rest-auth URLs
    path('auth/', include('dj_rest_auth.urls')),  
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  

    # OAuth2 URLs
    path('oauth/', include(('rest_framework_social_oauth2.urls', 'oauth2_provider'), namespace='oauth2_provider')),
    path('authorize/', views.authorize, name='authorize'),
    path('admin/login/', views.token, name='token'),

    # Social Django URLs for Twitter/Facebook login
    path('social-auth/', include('social_django.urls', namespace='social')),

    # Social Integration URLs (specific to your app)
    path('social_integration/', include('social_integration.urls')),

    # Index view (your core landing page)
    path('', IndexView.as_view(), name='index'),

    # Serve the React app for any other URLs
    path('dashboard/', dashboard_view, name='dashboard'),

    # Fallback to serve React app for unmatched URLs (optional, if you're handling routing in React)
    path('', TemplateView.as_view(template_name='index.html')),
]

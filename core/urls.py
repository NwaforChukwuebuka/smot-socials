from django.urls import path
from . import views
from django.urls import path
from .views import test_api


urlpatterns = [
    path('', views.index, name='home'),
    path('test-api/', test_api, name='test_api'),
]

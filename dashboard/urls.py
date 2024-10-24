from django.urls import path
from .views import dashboard_view

urlpatterns = [
    # Other URL patterns...
    path('dashboard/', dashboard_view, name='dashboard'),
]

# In your views.py (e.g., dashboard/views.py)

from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'build/index.html')  # Serve the React app



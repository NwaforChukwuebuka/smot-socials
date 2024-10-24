from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if settings.DEBUG:  # When in development, redirect to React's dev server
            return redirect('http://localhost:3000/')
        return super().get(request, *args, **kwargs)

def test_api(request):
    return JsonResponse({"message": "Hello from Django!"})

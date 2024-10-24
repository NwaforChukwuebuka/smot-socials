from django.shortcuts import render
from django.http import JsonResponse

from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')
# Create your views here.
def home(request):
    return HttpResponse("Welcome to SMOT Socials Homepage")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if settings.DEBUG:  # When in development, redirect to React's dev server
            return redirect('http://localhost:3000/')
        return super().get(request, *args, **kwargs)

def test_api(request):
    return JsonResponse({"message": "Hello from Django!"})

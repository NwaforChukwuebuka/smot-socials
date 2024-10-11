from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')
# Create your views here.
def home(request):
    return HttpResponse("Welcome to SMOT Socials Homepage")

def test_api(request):
    return JsonResponse({"message": "Hello from Django!"})

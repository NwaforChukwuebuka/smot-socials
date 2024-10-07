from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')
# Create your views here.

def test_api(request):
    return JsonResponse({"message": "Hello from Django!"})

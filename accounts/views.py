from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegistrationForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
    else:
        form = LoginForm()
    return render(request, 'accounts/index.html', {'form': form, 'form_type': 'login'})

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'accounts/index.html', {'form': form, 'form_type': 'register'})

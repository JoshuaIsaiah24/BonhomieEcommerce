from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "There was an error logging in, try again...")
            return redirect("log-in")
    else:
        return render(request, 'register/login.html', {})

def register_user(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            messages.success(request, "User registered successfully! Please try logging in...")
            return redirect("log-in")
    else:
        register_form = RegisterForm()
    return render(request, 'register/login.html', {'register_form':register_form})
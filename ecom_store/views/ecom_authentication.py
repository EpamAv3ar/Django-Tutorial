from django.shortcuts import render, redirect
from ecom_store.forms import SignUpForm, SignInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered successfully")
            return redirect('home')
        else:
            messages.error(request, "Error while registering user...")
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in !!!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username and password")
                return redirect('login')
    else:
        form = SignInForm()
    return render(request, 'authentication/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('login')

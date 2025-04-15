from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                cd['username'], cd['email'], cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(
                request, 'user registered successfully', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'your successfully login', 'success')
                return redirect('home')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'your successfully logout', 'success')
    return redirect('home')

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.


def list(request):
    return render(request, 'frontend/list.html')


def registration(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        #TODO refactor error handling, complex password only

    context = {'form': form}
    return render(request, 'frontend/registration.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
    return render(request, 'frontend/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login_page')


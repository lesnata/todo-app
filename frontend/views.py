from django.shortcuts import render
from djoser.serializers import UserCreateSerializer
# Create your views here.


def list(request):
    return render(request, 'frontend/list.html')


def registration(request):
    return render(request, 'frontend/registration.html')

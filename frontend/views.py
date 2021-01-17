from django.shortcuts import render
#from djoser.serializers import UserCreateSerializer
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def list(request):
    return render(request, 'frontend/list.html')


def registration(request):
    form = UserCreationForm()
    context = {'form': form}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    return render(request, 'frontend/registration.html', context)

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# views here...
from .models import *


def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)

def loginPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)

def homePage(request):
    context = {}
    return render(request, 'account/home.html', context)
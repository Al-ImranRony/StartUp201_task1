from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# views here...
from .models import *
from .forms import CreateUserForm


def registerPage(request):        
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'account/register.html', context)
        

def loginPage(request):
    if request.method == 'POST':
        form = UserCreationForm()
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    context = {}
    return render(request, 'account/login.html', context)

def indexPage(request):
    context = {}
    return render(request, 'account/index.html', context)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def homePage(request):
    context = {}
    return render(request, 'account/home.html', context)
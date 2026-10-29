from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import RegisterForm


User = get_user_model()

# Create your views here.
def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            a = form.get_user()
            login(request, a)
            print("Hello")    
    else:
        form = AuthenticationForm()

    return render(request,'home.html',{"form" : form})

def apple(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request,'apple.html',{"form":form})
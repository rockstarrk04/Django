from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login,logout, update_session_auth_hash

# Create your views here.
def login_(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" :
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    return render(request,'login.html',{"form" : form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_')
    else:
        form = RegisterForm()
    return render(request,'register.html',{"form" : form})

def logout_(request):
    logout(request)
    return redirect('login_')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('login_')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})
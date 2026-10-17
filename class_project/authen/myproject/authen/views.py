from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def login_(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)
        if user:
            login(request,user)
            messages.success(request,"Login Successful..!!")
            return redirect('home')
        else:
            messages.error(request,"Username or Password is Incorrect")
            return redirect('login_')

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
            return render(request,'register.html',{"msz" : 'username already exist!!'})
        
        except:
            User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password,
            )
            return redirect('login_')
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def logout_(request):
    logout(request)
    messages.success(request,"logged out successfully..!!")
    return redirect('home')  

def profile(request):
    return render(request,'profile.html')

def reset_password(request):
    
    global username
    username = request.user.username
    user = User.objects.get(username = request.user.username)
    if request.method == "POST":
        if 'old_password' in request.POST:
            old_password = request.POST['old_password']
            user = authenticate(username=request.user.username, password=old_password)
            if user :
                messages.success(request,'Enter New Password')
                return render(request,'reset_password.html',{"new" : True})
            else:
                messages.error(request,"Old password is incorrect")
                return render(request, 'reset_password.html')

        if 'new_password' in request.POST:
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully. Please log in again.')
                return redirect('login_')
            else:
                messages.error(request, 'New Password is not Matching... Please try again.')
                return redirect('reset_password')
    return render(request,'reset_password.html',{"data" : username})



def update(request):
    user = User.objects.get(username = request.user.username)
    if 'username' in request.POST:

        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']

            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            messages.success(request,'Updated Profile Successfully..!!')
            return redirect('profile')
    
    return render(request,'update.html',{"data" : user})


def forgot_password(request):
    global username
    if request.method == "POST":
        if 'username' in request.POST:
            username = request.POST['username']
            try:
                if User.objects.get(username = username) : 
                    return render(request,'forgot_password.html',{"new" : True})
            except:
                messages.error(request,"User Doesn't Exist..!")

        if 'password' in request.POST:
            new_password = request.POST['password']
            user = User.objects.get(username = username)
            user.set_password(new_password)
            user.save()
            messages.success(request,'Successfully Changed Password..!')
            return redirect('login_')
    return render(request,'forgot_password.html')
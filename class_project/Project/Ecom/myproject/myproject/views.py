from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def electronics(request):
    return render(request,'electronics.html')

def fashion(request):
    return render(request,'fashion.html')

def mobiles(request):
    return render(request,'mobiles.html')

def fresh(request):
    return render(request,'fresh.html')

def healthcare(request):
    return render(request,'healthcare.html')

def about(request):
    return render(request,'about.html')
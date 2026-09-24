from django.http import HttpResponse
from django.shortcuts import render

def sheela(request):
    return HttpResponse("Hello")

def sweety(request):
    return render(request,"sweety.html")

def chintu(request):
    return render(request,"chintu.html")

def chigari(request):
    return render(request,"chigari.html")
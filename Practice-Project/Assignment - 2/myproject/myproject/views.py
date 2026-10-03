from django.shortcuts import render

def audi(request):
    return render(request,'audi.html')

def bmw(request):
    return render(request,'bmw.html')

def ferrari(request):
    return render(request,'ferrari.html')

def dragon(request):
    return render(request,'dragon.html')

def kiwi(request):
    return render(request,'kiwi.html')
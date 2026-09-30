from django.shortcuts import render

def banana(request):
    return render(request , 'banana.html')

def apple(request):
    return render(request , 'apple.html')

def chintu(request):
    return render(request , 'chintu.html')

def sheela(request):
    return render(request , 'sheela.html')

def papaya(request):
    return render(request , 'papaya.html')
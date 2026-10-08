from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def apple(request):
    return render(request,'apple.html')

def banana(request):
    return render(request,'banana.html')
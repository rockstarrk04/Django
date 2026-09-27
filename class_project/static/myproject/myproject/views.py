from django.shortcuts import render

def inline_CSS(request):
    return render(request,'inline_CSS.html')

def internal_CSS(request):
    return render(request,'internal_CSS.html')

def external_CSS(request):
    return render(request,'external_CSS.html')

def django_external_CSS(request):
    return render(request,'django_external_CSS.html')

def image(request):
    return render(request,'image.html')

def django_image(request):
    return render(request,'django_image.html')
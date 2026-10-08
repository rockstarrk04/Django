from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def student(request,id):
    if id == 1:
        return HttpResponse("details of student 1")
    if id == 2:
        return HttpResponse("details of student 2")
    if id == 3:
        return HttpResponse("details of student 3")
    if id == 4:
        return HttpResponse("details of student 4")
    if id == 5:
        return HttpResponse("details of student 5")
    else:
        return HttpResponse("no details")

def employee(request,name):
    if name == "A":
        return HttpResponse("details of A")
    if name == "B":
        return HttpResponse("details of B")
    if name == "C":
        return HttpResponse("details of C")
    if name == "D":
        return HttpResponse("details of D")
    if name == "E":
        return HttpResponse("details of E")
    else:
        return HttpResponse("no details")

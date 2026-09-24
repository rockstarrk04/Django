from django.http import HttpResponse 

def sheela(request):
    return HttpResponse("Hello how are you all")

def apple(request):
    return HttpResponse("One Apple a day, keeps the Doctor Away")

def banana(request):
    return HttpResponse("<h1>Hello I'm Banana</h1>")

def list(request):
    list_Data = [1,2,3,4,5,"abc",True,1.23,{"color" : "red"}]
    return HttpResponse(list_Data)

def add(request):
    a = 10
    b = 20
    c = a + b
    return HttpResponse(c)
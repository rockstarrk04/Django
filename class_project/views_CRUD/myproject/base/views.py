from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    # data = CarModel.objects.get(id=1)
    data_all = CarModel.objects.all()

    # data_filter = CarModel.objects.get(car_name__icontains = 'a')
    # data_all = CarModel.objects.filter(color = 'abc')    
    # data_filter = CarModel.objects.filter(car_name__icontains = 'xyz')

    context = {"data_all" : data_all}
    return render(request,'home.html',context)


def add(request):
    print(request)  #! <WSGIRequest: GET '/add/'>
    print(request.method) # !GET


    if 'car_name' in request.GET:
        print('IF condition')
        print(request)
        print(request.method)

        # request.GET['car_name']
        # request.GET['color']
        # request.GET['price']

        a = request.GET['car_name']
        b = request.GET['color']
        c = request.GET['price']

        print(a,b,c)

        CarModel.objects.create(
            car_name = a,
            color = b,
            price = c
        )


    if request.method == 'POST':
        print('IF condition')
        print(request)
        print(request.method)
        # request.POST['car_name']
        # request.POST['color']
        # request.POST['price']

        d = request.POST['car_name']
        e = request.POST['color']
        f = request.POST['price']

        print(d,e,f)

        CarModel.objects.create(
            car_name = d,
            color = e,
            price = f
        )
    return render(request,'add.html')

def hdelete(request,pk):
    data = CarModel.objects.get(id = pk)
    data.delete()
    return redirect('home')


def update(request,pk):
    data = CarModel.objects.get(id = pk)

    if request.method == "POST" :
        a = request.POST['car_name']
        b = request.POST['color']
        c = request.POST['price']

        data.car_name = a
        data.color = b
        data.price = c
        data.save()
        return redirect('home')

    return render(request,'update.html',{"data" : data})

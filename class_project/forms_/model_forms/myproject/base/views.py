from django.shortcuts import render,get_object_or_404,redirect
from .forms import CarForm
from .models import CarModel

# Create your views here.
def home(request):
    if request.method == "POST":
        form_data = CarForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        
    form = CarForm()
    data = CarModel.objects.all()
    context = {
        "form" : form,
        "data" : data
    }   

    return render(request,'home.html',context)


def update(request,pk):
    data = get_object_or_404(CarModel,id = pk)
    form = CarForm(instance = data)
    

    if request.method == "POST" :
        form = CarForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        "form" : form,
        "data" : data
    }

    return render(request,'update.html',context)
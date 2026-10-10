from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    data = CarModel.objects.get(id=1)
    data_all = CarModel.objects.all()
    context = {'data':data , "data_all" : data_all}
    
    return render(request,'home.html', context)
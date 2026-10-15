from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    data = StudentModel.objects.all()
    if request.method == 'POST':
        s_name = request.POST['s_name']
        reg_no = request.POST['reg_no'] 
        image = request.FILES.get('image') 

        StudentModel.objects.create(
            s_name = s_name,
            reg_no = reg_no,
            image = image if image else 'thor.jpg'
        )


    return render(request,'home.html',{'data' : data})
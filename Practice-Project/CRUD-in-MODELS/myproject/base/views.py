from django.shortcuts import render
from .models import StudentModel

# Create your views here.
def home(request):
    data = StudentModel.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        image = request.FILES.get['image']  

        StudentModel.objects.create(
            std_name = name,
            age = age,
            image = image if image else 'img4.png'
        )

    return render(request,'home.html',{'data':data})
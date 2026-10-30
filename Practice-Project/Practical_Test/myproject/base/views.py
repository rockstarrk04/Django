from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel,TrashModel

# Create your views here.
def home(request):
    data = StudentModel.objects.all()
    
    return render(request,'home.html',{"data":data})

def add(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        course = request.POST['course']
        city = request.POST['city']

        StudentModel.objects.create(
            name = name,
            email = email,
            mobile_number = mobile_number,
            course = course,
            city = city
        )
        return redirect('home')
    
    else:
        form = StudentForm()

    return render(request,'add.html',{"form" : form})


def update(request,pk):
    data = StudentModel.objects.get(id=pk)

    if request.method == "POST":
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.mobile_number = request.POST['mobile_number']
        data.course = request.POST['course']
        data.city = request.POST['city']

        data.save()

        return redirect('home')
    
    return render(request,'update.html',{"data":data})

def delete(request,pk):
    data = StudentModel.objects.get(id = pk)

    TrashModel.objects.create(
        name = data.name,
        email = data.email,
        mobile_number = data.mobile_number,
        course = data.course,
        city = data.city
    )
    data.delete()

    return redirect('home')

def trash(request):
    data = TrashModel.objects.all()
    return render(request,'trash.html',{"data":data})

def restore(request,pk):
    data = TrashModel.objects.get(id=pk)

    StudentModel.objects.create(
        name = data.name,
        email = data.email,
        mobile_number = data.mobile_number,
        course = data.course,
        city = data.city
    )
    data.delete()
    
    return redirect('trash')
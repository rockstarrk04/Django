from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import TodoModel


# Create your views here.
@login_required(login_url='login_')
def home(request):
    data = TodoModel.objects.filter(is_delete = False,user = request.user)
    print(data)
    return render(request,'home.html',{"data" : data})

@login_required(login_url='login_')
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        user = request.user

        TodoModel.objects.create(
            title = title,
            desc = desc,
            user= user
        )
    return render(request,'add.html')

@login_required(login_url='login_')
def hdelete(request,pk):
    data = TodoModel.objects.get(id = pk)
    data.is_delete = True
    data.save()

    return redirect('trash')

@login_required(login_url='login_')
def trash(request):
    data = TodoModel.objects.filter(is_delete = True,user = request.user)

    return render(request,'trash.html',{"data":data})

@login_required(login_url='login_')
def hrestore(request,pk):
    data = TodoModel.objects.get(id = pk)
    data.is_delete = False
    data.save()

    return redirect('home')

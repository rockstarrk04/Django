from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    data = TodoModel.objects.all()
    context = {"data" : data}
    return render(request,'home.html',context)

def add(request):
    if request.method == 'POST':
        a = request.POST['title']
        b = request.POST['desc']

        TodoModel.objects.create(
            title = a,
            desc = b
        )
    return render(request,'add.html')

def complete(request):
    data = CompleteTodoModel.objects.all()
    return render(request,'complete.html',{"data" : data})

def trash(request):
    data = TrashModel.objects.all()
    return render(request,'trash.html',{"data" : data})

def about(request):
    return render(request,'about.html')

def update(request,pk):
    data = TodoModel.objects.get(id=pk)

    if request.method == "POST":
        a = request.POST['title']
        b = request.POST['desc']

        data.title = a
        data.desc = b
        data.save()
        return redirect('home')
    
    return render(request,'update.html',{"data" : data})

def delete(request,pk):
    data = TodoModel.objects.get(id = pk)
    data.delete()
    return redirect('home')

def hcomplete(request,pk):
    data = TodoModel.objects.get(id = pk)

    CompleteTodoModel.objects.create(
        title = data.title,
        desc = data.desc
    )

    data.delete()

    return redirect('home')

def hdelete(request,pk):
    data = TodoModel.objects.get(id=pk)

    TrashModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()

    return redirect('home')

def complete_all(request):
    data = TodoModel.objects.all()

    for i in data:
        CompleteTodoModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()

    return redirect('home')

def delete_all(request):
    data = TodoModel.objects.all()

    for i in data:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc,
        )
        i.delete()
    return redirect('home')


def trestore_all(request):
    data = TrashModel.objects.all()

    for i in data:
        TodoModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('trash')


def delete_all(request):
    data = TodoModel.objects.all()
    
    for i in data:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    
    return redirect('home')

def cdelete_all(request):
    data = CompleteTodoModel.objects.all()

    for i in data:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('complete')

def crestore_all(request):
    data = CompleteTodoModel.objects.all()

    for i in data:
        TodoModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('complete')

def cdelete(request,pk):
    data = CompleteTodoModel.objects.get(id=pk)
    TrashModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('complete')

def crestore(request,pk):
    data = CompleteTodoModel.objects.get(id=pk)

    TodoModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()

    return redirect('complete')

def tdelete_all(request):
    data = TrashModel.objects.all()
    
    for i in data:
        i.delete()
    
    return redirect('trash')

def tdelete(request,pk):
    data = TrashModel.objects.get(id=pk)
    data.delete()

    return redirect('trash')

def trestore(request,pk):
    data = TrashModel.objects.get(id=pk)
    TodoModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()

    return redirect('trash')
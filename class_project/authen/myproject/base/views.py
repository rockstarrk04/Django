from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import TodoModel
from authen.models import PictureModel
from authen.views import profile_image
from django.db.models import Q
from django.contrib import messages

# Create your views here.
@login_required(login_url='login_')
def home(request):
    mgz = False
    count = False
    count = TodoModel.objects.filter(user = request.user , is_delete = False).count()
    profile = profile_image(request)

    if 'q' in request.GET:
        q = request.GET['q']
        if q.isdigit():
            data = TodoModel.objects.filter(Q(id = int(q)) & Q( user = request.user) & Q(is_delete = False))
        else:
            data = TodoModel.objects.filter(
                Q(title__icontains = q) & Q( user = request.user) & Q(is_delete = False) |
                Q(desc__icontains = q) & Q( user = request.user) & Q(is_delete = False)
            )

        if len(data) == 0 :
            messages.error(request,"No Records Found !!!")
            mgz = True
                
    else:
        data = TodoModel.objects.filter(is_delete = False,user = request.user)
    return render(request,'home.html',{"data" : data , "profile" : profile , "mgz" : mgz})

@login_required(login_url='login_')
def add(request):
    profile = profile_image(request)
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        user = request.user

        TodoModel.objects.create(
            title = title,
            desc = desc,
            user= user
        )
    return render(request,'add.html',{"profile" : profile})

@login_required(login_url='login_')
def hdelete(request,pk):
    data = TodoModel.objects.get(id = pk)
    data.is_delete = True
    data.save()

    return redirect('home')

@login_required(login_url='login_')
def hcomplete(request,pk):
    data = TodoModel.objects.get(id = pk)
    data.is_complete = True
    data.save()
    return redirect('home')


@login_required(login_url='login_')
def trash(request):
    profile = profile_image(request)
    data = TodoModel.objects.filter(is_delete = True,user = request.user)

    return render(request,'trash.html',{"data":data , "profile" : profile})

@login_required(login_url='login_')
def hrestore(request,pk):
    data = TodoModel.objects.get(id = pk)
    data.is_delete = False
    data.save()

    return redirect('trash')
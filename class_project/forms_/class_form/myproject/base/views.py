from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel

# Create your views here.
def home(request):
    form = StudentForm()
    data = StudentModel.objects.all()
    context = {
        "form" : form,
        "data" : data
    }

    # if request.method == 'POST':
    #     std_name = request.POST['std_name']
    #     std_number = request.POST['std_number']
    #     std_email = request.POST['std_email']

    #     StudentModel.objects.create(
    #         name = std_name,
    #         phone = std_number,
    #         email = std_email
    #     )

    if request.method == 'POST':            
        form_data = StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()

    return render(request,'home.html',context)


def update(request,pk):
    data = StudentModel.objects.get(id = pk)    
    form = StudentForm(initial = {
        "Name" : data.name,
        "Number" : data.phone,
        "Email" : data.email
    })

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.update(data)
            return redirect('home')

    return render(request,'update.html',{"form" : form})

def form_display(request):
    form = StudentForm()
    context = {"form" : form}
    return render(request,'form_display.html',context)
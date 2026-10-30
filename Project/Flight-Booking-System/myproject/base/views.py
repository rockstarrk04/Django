from django.shortcuts import render,redirect
from .models import FlightModel,TicketBookingModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.
@login_required(login_url='login_')
def home(request):
    if request.method == "GET":
        data = FlightModel.objects.filter(is_available = True)
        source = request.GET.get('source', '').strip()
        destination = request.GET.get('destination', '').strip()

        if source:
            data = data.filter(source__icontains=source)
        if destination:
            data = data.filter(destination__icontains=destination)

    return render(request, 'home.html', {
        "data": data,
        "source": source,
        "destination": destination,
    })

@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')

def book(request,pk):
    data = FlightModel.objects.get(id=pk)

    if request.method == "POST":
        c_name = request.POST['c_name']
        c_email = request.POST['c_email']
        c_phone_no = request.POST['c_phone_no']
        c_adhaar_no = request.POST['c_adhaar_no']
        c_age = request.POST['c_age']
        seat_class = request.POST['seat_class']
        seat_no = request.POST['seat_no']

        TicketBookingModel.objects.create(
            company=data.company,
            flight_name=data.flight_name,
            flight_number=data.flight_number,
            source=data.source,
            destination=data.destination,
            departure_time=data.departure_time,
            date=data.date,
            price=data.price,
            c_name=c_name,
            c_email=c_email,
            c_phone_no=c_phone_no,
            c_adhaar_no=c_adhaar_no,
            c_age=c_age,
            seat_class=seat_class,
            seat_no=seat_no,
            user=request.user,
        )
        return redirect('home')
    
    return render(request,'book.html',{"data":data})

@login_required(login_url='login_')
def bookings(request):
    data = TicketBookingModel.objects.filter(user=request.user)
    return render(request,'showBooking.html',{"data":data})

def cancel_ticket(request,pk):
    data = TicketBookingModel.objects.get(id = pk)
    data.delete()
    return redirect('bookings')

def update_ticket(request,pk):
    data = TicketBookingModel.objects.get(id=pk)
    
    if request.method == "POST":

        data.c_name = request.POST['c_name']
        data.c_email = request.POST['c_email']
        data.c_phone_no = request.POST['c_phone_no']
        data.c_adhaar_no = request.POST['c_adhaar_no']
        data.c_age = request.POST['c_age']
        data.seat_class = request.POST['seat_class']
        data.seat_no = request.POST['seat_no']

        data.save()
        return redirect('bookings')
    
    return render(request,'update_ticket.html',{"data":data})


def update_profile(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=user)

    return render(request, 'update_profile.html', {'form': form})

def history(request):
    return render(request,'history.html')

def support(request):
    return render(request,'support.html')

def about(request):
    return render(request,'about.html')
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FlightModel(models.Model):
    company = models.CharField(max_length=50)
    flight_name = models.CharField(max_length=50)
    flight_number = models.IntegerField()
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.TimeField()
    date = models.DateTimeField()
    price = models.IntegerField()
    is_available = models.BooleanField()


class TicketBookingModel(models.Model):
    company = models.CharField(max_length=50)
    flight_name = models.CharField(max_length=50)
    flight_number = models.IntegerField()
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.TimeField()
    date = models.DateTimeField()
    price = models.IntegerField()
    c_name = models.CharField(max_length=50)
    c_email = models.EmailField()
    c_phone_no = models.IntegerField()
    c_adhaar_no = models.IntegerField()
    c_age = models.IntegerField()
    seat_class = models.CharField()
    seat_no = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
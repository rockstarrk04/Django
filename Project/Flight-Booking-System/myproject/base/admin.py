from django.contrib import admin
from .models import FlightModel
# Register your models here.

@admin.register(FlightModel)
class FlightAdmin(admin.ModelAdmin):
    model = FlightModel
    list_display = ['id','company','flight_name','flight_number','source','destination','departure_time','date','price',"is_available"]
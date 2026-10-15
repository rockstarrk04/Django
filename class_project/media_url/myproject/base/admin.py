from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    model = StudentModel
    list_display = ['id' , 's_name' , 'reg_no' , 'image']
    search_fields = ['reg_no']
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    model = StudentModel
    list_display = ['id' , 'std_name' , 'course' , 'age' , 'email']
    search_fields = ['std_name']


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    model = EmployeeModel
    list_display = ['id' , 'e_name' , 'dept' , 'salary' , 'email' , 'description' , 'experience' , 'doj' , 'login_time' , 'joining' , 'is_active' , 'website','price' ]
    search_fields = ['e_name']


# admin.site.register(StudentModel , StudentAdmin)
# admin.site.register(EmployeeModel)


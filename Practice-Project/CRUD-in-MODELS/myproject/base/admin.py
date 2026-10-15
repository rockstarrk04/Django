from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    model = StudentModel
    list_display = ['id' ,'std_name' , 'age' ,'image']
#     search_fields = ['id']
#     list_filter = ['age' ]
#     ordering = ['id']  # used for sorting
#     list_editable = ['age',]  # used for editing values without entering into object
#     list_display_links = ['std_name' , 'id']  # used to select an model Object (record)
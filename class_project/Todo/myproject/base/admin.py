from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    model = TodoModel
    list_display = ['id' , 'title' , 'desc']

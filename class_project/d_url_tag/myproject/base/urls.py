from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('student/<int:id>',student,name='student'),
    path('employee/<name>',employee,name="employee")
]
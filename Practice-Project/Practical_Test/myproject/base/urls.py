from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('add/',add,name="add"),
    path('update/<int:pk>',update,name="update"),
    path('delete/<int:pk>',delete,name="delete"),
    path('trash/',trash,name="trash"),
    path('restore/<int:pk>',restore,name="restore"),
]
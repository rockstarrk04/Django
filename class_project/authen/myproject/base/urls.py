from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('add/',add,name="add"),
    path('hdelete/<int:pk>',hdelete,name="hdelete"),
    path('hrestore/<int:pk>',hrestore,name="hrestore"),
    path('trash',trash,name="trash")
]
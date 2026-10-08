from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('apple/',apple,name="apple"),
    path('banana/',banana,name="banana")
]
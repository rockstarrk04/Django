from django.urls import path
from .views import *


urlpatterns = [
    path('home/',home,name="home"),
    path('mobile/',mobile,name="mobile"),
    path('laptop/',laptop,name="laptop")
]

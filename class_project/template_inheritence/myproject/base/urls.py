from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name="home"),
    path('fashion/',fashion,name="fashion"),
    path('about/',about,name="about")
]
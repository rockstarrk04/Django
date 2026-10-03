from django.urls import path
from .views import *

urlpatterns = [
    path('apple/',apple),
    path('banana/',banana)
]
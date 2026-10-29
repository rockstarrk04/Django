from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name="login_"),
    path('register',register,name="register")
]
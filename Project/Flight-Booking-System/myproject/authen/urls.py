from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name="login_"),
    path('register/',register,name="register"),
    path('logout/',logout_,name="logout_"),
    path('change_password',change_password,name="change_password")

]
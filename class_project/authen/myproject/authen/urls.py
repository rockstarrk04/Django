from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name="login_"),
    path('register/',register,name="register"),
    path('profile/',profile,name="profile"),
    path('logout',logout_,name="logout_"),
    path('reset_password',reset_password,name="reset_password"),
    path('update',update,name="update"),
    path('forgot_password/',forgot_password,name="forgot_password")  
]
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('add/',add,name="add"),
    path('complete/',complete,name="complete"),
    path('trash/',trash,name="trash"),
    path('about/',about,name="about"),
    path('update/<int:pk>',update,name="update"),
    path('delete/<int:pk>',delete,name="delete"),
    path('delete_all/',delete_all,name="delete_all"),
    path('hdelete/<int:pk>',hdelete,name="hdelete"),
    path('hcomplete/<int:pk>',hcomplete,name="hcomplete"),
    path('cdelete_all/',cdelete_all,name="cdelete_all"),
    path('crestore_all/',crestore_all,name="crestore_all"),
    path('cdelete/<int:pk>',cdelete,name="cdelete"),
    path('crestore/<int:pk>',crestore,name="crestore"),
    path('trestore_all/',trestore_all,name="trestore_all"),
    path('tdelete_all/',tdelete_all,name="tdelete_all"),
    path('trestore/<int:pk>',trestore,name="trestore"),
    path('tdelete/<int:pk>',tdelete,name="tdelete"),

]
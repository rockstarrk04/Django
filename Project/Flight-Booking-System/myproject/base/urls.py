from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('profile/',profile,name="profile"),
    path('book/<int:pk>',book,name="book"),
    path('bookings/',bookings,name="bookings"),
    path('cancel_ticket/<int:pk>',cancel_ticket,name="cancel_ticket"),
    path('update_ticket/<int:pk>',update_ticket,name="update_ticket"),
    path('update_profile',update_profile,name="update_profile"),
    path('history',history,name="history"),
    path('support',support,name="support"),
    path('about',about,name="about"),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('news/',news,name="news"),
    path('sports/',sports,name="sports"),
    path('international/',international,name="international"),
    path('blogs/',blogs,name="blogs"),
    path('about/',about,name="about"),
    path('home_read/<int:id>',home_read,name="home_read"),
    path('news_read/<int:id>',news_read,name="news_read"),
    path('sports_read<int:id>',sports_read,name="sports_read"),
    path('international_read<int:id>',international_read,name="international_read"),
    path('blogs_read<int:id>',blogs_read,name="blogs_read"),
    path('about_read<int:id>',about_read,name="about_read"),
]
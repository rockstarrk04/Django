"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import palindrome , even_or_odd , prime_number , check_number, factorial, sum_of_digits

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', even_or_odd),
    path('2/', palindrome),
    path('3/', prime_number),
    path('4/', check_number),
    path('5/', factorial),
    path('6/', sum_of_digits)
]
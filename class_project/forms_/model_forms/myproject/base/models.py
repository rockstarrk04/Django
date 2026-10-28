from django.db import models

# Create your models here.
class CarModel(models.Model):
    car = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    price = models.IntegerField()
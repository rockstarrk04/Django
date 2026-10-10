from django.db import models

# Create your models here.
class FruitModel(models.Model):
    fruitname = models.CharField(max_length=30)
    price = models.IntegerField()
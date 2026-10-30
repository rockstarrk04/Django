from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=40)
    email = models .EmailField()
    mobile_number = models.IntegerField()
    course = models.CharField(max_length=40)
    city = models.CharField(max_length=40)

class TrashModel(models.Model):
    name = models.CharField(max_length=40)
    email = models .EmailField()
    mobile_number = models.IntegerField()
    course = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.EmailField()
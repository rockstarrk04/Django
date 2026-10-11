from django.db import models

# Create your models here.
class StudentModel(models.Model):
    std_name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()
    dob = models.DateField()
    USN = models.IntegerField()
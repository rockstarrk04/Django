from django.db import models

# Create your models here.
class StudentModel(models.Model):
    std_name = models.CharField(max_length=30)
    course = models.CharField(max_length=40)
    mobile = models.IntegerField(10,null=True)

class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(2)
    gender = models.CharField()
    sal = models.IntegerField()
    address = models.CharField()
    phone_no = models.IntegerField()
    email = models.EmailField()
    dept = models.CharField()
    dob = models.DateField()
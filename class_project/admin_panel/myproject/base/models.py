from django.db import models

# Create your models here.
class StudentModel(models.Model):
    std_name = models.CharField(max_length=40)
    course = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

class EmployeeModel(models.Model):
    e_name = models.CharField(max_length=40,null=True)
    dept = models.CharField(max_length=50,null=True)
    salary = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=10.00)
    experience = models.FloatField(null=True)
    doj = models.DateField(null=True)
    login_time = models.TimeField(null=True)
    joining = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    # resume_pdf = models.FileField(upload_to='files/')
    website = models.URLField(null=True)






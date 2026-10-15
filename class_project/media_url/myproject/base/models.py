from django.db import models

# Create your models here.
class StudentModel(models.Model):
    s_name = models.CharField(max_length=40)
    reg_no = models.IntegerField()
    image = models.ImageField(upload_to='upload/',default='thor.jpg')

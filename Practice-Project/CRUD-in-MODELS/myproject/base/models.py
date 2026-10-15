from django.db import models

# Create your models here.
class StudentModel(models.Model):
    std_name = models.CharField(max_length=30)
    age = models.IntegerField()
    image  = models.ImageField(upload_to='upload/',default='img4.png')
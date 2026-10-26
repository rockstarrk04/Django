from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    is_delete = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
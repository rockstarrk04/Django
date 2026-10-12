from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=40)
    desc = models.TextField()

class CompleteTodoModel(models.Model):
    title = models.CharField(max_length=40)
    desc = models.TextField()

class TrashModel(models.Model):
    title = models.CharField(max_length=40)
    desc = models.TextField()
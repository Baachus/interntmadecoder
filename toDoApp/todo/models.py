from django.db import models

# Create your models here.

class TaskModel(models.Model):
    '''This class is used to create the model for the todo app.'''
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    priority = models.IntegerField()

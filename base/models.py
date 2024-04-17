from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    status = models.CharField(max_length=50)

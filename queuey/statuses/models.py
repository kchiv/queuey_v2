from django.db import models

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=100)

class Priority(models.Model):
    priority = models.CharField(max_length=100)
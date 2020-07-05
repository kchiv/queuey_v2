from django.db import models

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.status

class Priority(models.Model):
    priority = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'priorities'

    def __str__(self):
        return self.priority
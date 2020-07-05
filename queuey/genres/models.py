from django.db import models

# Create your models here.

class Genre(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=300)
from django.db import models

# Create your models here.

class Genre(models.Model):
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
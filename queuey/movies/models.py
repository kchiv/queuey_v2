from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=500)
    tmdb_id = models.IntegerField()
    imdb_id = models.CharField(max_length=500)
    movie_description = models.TextField()
    poster_url = models.URLField()
    release_date = models.DateField()
    rating = models.FloatField()
    # status =
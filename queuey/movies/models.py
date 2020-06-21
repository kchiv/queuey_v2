from django.db import models
from statuses.models import Status, Priority

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=500)
    tmdb_id = models.IntegerField()
    imdb_id = models.CharField(max_length=500)
    movie_description = models.TextField()
    poster_url = models.URLField()
    release_date = models.DateField()
    rating = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    watched_date = models.DateField()
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    notes = models.TextField()
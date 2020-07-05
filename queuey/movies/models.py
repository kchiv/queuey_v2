from django.db import models
from genres.models import Genre
from statuses.models import Status, Priority

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=500)
    overview = models.TextField()
    tmdb_id = models.IntegerField()
    poster_url = models.URLField()
    backdrop_url = models.URLField()

class Movie(models.Model):
    title = models.CharField(max_length=500)
    tmdb_id = models.IntegerField()
    imdb_id = models.CharField(max_length=500)
    movie_description = models.TextField()
    tagline = models.TextField(null=True)
    poster_url = models.URLField()
    release_date = models.DateField()
    runtime = models.IntegerField(null=True)
    rating = models.FloatField()
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    collection = models.ManyToManyField(Collection, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    watched_date = models.DateField()
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    notes = models.TextField()
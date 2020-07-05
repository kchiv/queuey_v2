from django.db import models
from django.contrib.auth.models import User
from genres.models import Genre
from platforms.models import Platform
from statuses.models import Status, Priority

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=500)
    overview = models.TextField(null=True, blank=True)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    poster_url = models.CharField(max_length=500, null=True, blank=True)
    backdrop_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=500)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    imdb_id = models.CharField(max_length=500, null=True, blank=True, unique=True)
    movie_description = models.TextField(null=True, blank=True)
    tagline = models.TextField(null=True, blank=True)
    poster_url = models.CharField(max_length=500, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    collection = models.ManyToManyField(Collection, blank=True)

    def __str__(self):
        return self.title

class MovieUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    platforms = models.ManyToManyField(Platform, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    watched_date = models.DateField(null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user, self.movie
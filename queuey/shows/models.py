from django.db import models
from django.contrib.auth.models import User
from genres.models import Genre
from platforms.models import Platform
from statuses.models import Status, Priority

# Create your models here.

class Network(models.Model):
    name = models.CharField(max_length=300)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    origin_country = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class TvShow(models.Model):
    name = models.CharField(max_length=500)
    original_name = models.CharField(max_length=500)
    show_description = models.TextField(null=True, blank=True)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    first_air_date = models.DateField(null=True, blank=True)
    last_air_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    networks = models.ManyToManyField(Network, blank=True)
    poster_url = models.CharField(max_length=500, null=True, blank=True)
    backdrop_url = models.CharField(max_length=500, null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class TvSeason(models.Model):
    name = models.CharField(max_length=500)
    tv_show = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    air_date = models.DateField(null=True, blank=True)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    alt_id = models.CharField(max_length=500, null=True, blank=True, unique=True)
    season_description = models.TextField(null=True, blank=True)
    season_number = models.IntegerField(null=True, blank=True)
    poster_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class TvEpisode(models.Model):
    name = models.CharField(max_length=500)
    air_date = models.DateField(null=True, blank=True)
    episode_number = models.IntegerField(null=True, blank=True)
    episode_description = models.TextField(null=True, blank=True)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    tv_season = models.ForeignKey(TvSeason, on_delete=models.CASCADE)
    still_url = models.CharField(max_length=500, null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class TvUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv = models.ForeignKey(TvEpisode, on_delete=models.CASCADE)
    platforms = models.ManyToManyField(Platform, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    watched_date = models.DateField(null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    leaving_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user, self.movie
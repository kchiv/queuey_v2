from django.contrib import admin
from .models import Network, TvShow, TvSeason, TvEpisode, TvUser

# Register your models here.

admin.site.register(Network)
admin.site.register(TvShow)
admin.site.register(TvSeason)
admin.site.register(TvEpisode)
admin.site.register(TvUser)
# Generated by Django 3.0.7 on 2020-06-21 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statuses', '0002_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('tmdb_id', models.IntegerField()),
                ('imdb_id', models.CharField(max_length=500)),
                ('movie_description', models.TextField()),
                ('poster_url', models.URLField()),
                ('release_date', models.DateField()),
                ('rating', models.FloatField()),
                ('watched_date', models.DateField()),
                ('notes', models.TextField()),
                ('priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statuses.Priority')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statuses.Status')),
            ],
        ),
    ]

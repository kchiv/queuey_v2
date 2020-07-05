# Generated by Django 3.0.7 on 2020-07-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('overview', models.TextField()),
                ('tmdb_id', models.IntegerField()),
                ('poster_url', models.URLField()),
                ('backdrop_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='genres.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='vote_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='collection',
            field=models.ManyToManyField(blank=True, to='movies.Collection'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0001_initial'),
        ('movies', '0004_auto_20200705_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='platforms',
            field=models.ManyToManyField(blank=True, to='platforms.Platform'),
        ),
    ]
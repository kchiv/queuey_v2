# Generated by Django 3.0.7 on 2020-07-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200705_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline',
            field=models.TextField(null=True),
        ),
    ]
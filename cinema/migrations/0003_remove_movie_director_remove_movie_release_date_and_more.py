# Generated by Django 4.2.1 on 2024-04-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_movie_screeningroom_ticket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='release_datetime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='starring',
            field=models.CharField(default='', max_length=50),
        ),
    ]

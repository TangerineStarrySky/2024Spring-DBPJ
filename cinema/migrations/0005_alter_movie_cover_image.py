# Generated by Django 4.2.1 on 2024-04-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_alter_movie_release_datetime_alter_movie_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(upload_to='media/uploads'),
        ),
    ]

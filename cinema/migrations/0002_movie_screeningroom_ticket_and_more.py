# Generated by Django 4.2.1 on 2024-04-12 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=30, unique=True)),
                ('director', models.CharField(max_length=30)),
                ('starring', models.CharField(max_length=30)),
                ('cover_image', models.ImageField(upload_to='')),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ScreeningRoom',
            fields=[
                ('room_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=30, unique=True)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('movie_id', models.IntegerField()),
                ('room_id', models.IntegerField()),
                ('showtime', models.TimeField()),
                ('price', models.IntegerField()),
                ('seat_id', models.IntegerField()),
                ('evaluation', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='regdate',
            new_name='register_date',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
    ]

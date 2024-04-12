from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField(null=True)
    sex = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    register_date = models.DateField()


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=20, unique=True)
    starring = models.CharField(max_length=50)
    release_datetime = models.CharField(max_length=50)
    score = models.CharField(max_length=10)
    img = models.CharField(max_length=255, default='')

class ScreeningRoom(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=30, unique=True)
    seats = models.IntegerField()

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    room_id = models.IntegerField()
    showtime = models.TimeField()
    price = models.IntegerField()
    seat_id = models.IntegerField()
    evaluation = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

# Generated by Django 4.2.1 on 2024-04-13 05:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_screeningroom_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='evaluation',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='paytime',
            field=models.CharField(max_length=50),
        ),
    ]

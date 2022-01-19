from django.db import models
from database import create_choices


class Movies(models.Model):
    CHOICES_GENRES = create_choices()
    CHOICES_ROLES = [
        ("actor", "Actor"),
        ("actress", "Actress"),
        ("director", "Director")
    ]

    rating = models.FloatField(min_value=1, max_value=10)
    votes = models.IntegerField(min_value=1000, max_length=10)
    genre = models.CharField(choices=CHOICES_GENRES)
    prod_year = models.IntegerField(min_value=1850, min_length=4, max_length=4)
    role = models.CharField(choices=CHOICES_ROLES)
    name = models.CharField(max_length=128)
    birth_year = models.IntegerField(min_value=1800, min_length=4, max_length=4)


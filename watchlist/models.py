from django.db import models
from database import create_choices


class Movies(models.Model):
    CHOICES_GENRES = create_choices()
    CHOICES_ROLES = [
        ("actor", "Actor"),
        ("actress", "Actress"),
        ("director", "Director")
    ]

    rating = models.FloatField()
    votes = models.IntegerField(max_length=10)
    genre = models.CharField(choices=CHOICES_GENRES)
    prod_year = models.IntegerField(max_length=4)
    role = models.CharField(choices=CHOICES_ROLES)
    name = models.CharField(max_length=128)
    birth_year = models.IntegerField(max_length=4)

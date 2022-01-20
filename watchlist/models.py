from django.db import models
from database import create_choices
from watchlist.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator

class Movies(models.Model):
    CHOICES_GENRES = create_choices()
    CHOICES_ROLES = [
        ("actor", "Actor"),
        ("actress", "Actress"),
        ("director", "Director")
    ]

    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    votes = models.IntegerField(validators=[MinValueValidator(1000), MaxLengthValidator()])  # TODO insert value as max argument from database
    genre = models.CharField(max_length=32, choices=CHOICES_GENRES)
    prod_year = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator()]) # TODO insert datetime into func arg
    role = models.CharField(max_length=16, choices=CHOICES_ROLES)
    name = models.CharField(max_length=128)
    birth_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator()]) # TODO insert datetime into func arg


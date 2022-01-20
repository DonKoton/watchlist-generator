from django.db import models
from database import create_choices, get_max_votes_num
from watchlist.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Movies(models.Model):
    CHOICES_GENRES = create_choices()
    CHOICES_ROLES = [
        ("actor", "Actor"),
        ("actress", "Actress"),
        ("director", "Director")
    ]
    current_date = datetime.today().year

    rating = models.FloatField(validators=[MinValueValidator(1.0),
                                           MaxValueValidator(10.0)
                                           ]
                               )
    votes = models.IntegerField(validators=[MinValueValidator(1000),
                                            MaxValueValidator(get_max_votes_num())
                                            ]
                                )
    genre = models.CharField(max_length=32,
                             choices=CHOICES_GENRES
                             )
    prod_year = models.IntegerField(validators=[MinValueValidator(1960),
                                                MaxValueValidator(current_date)
                                                ]
                                    )
    role = models.CharField(max_length=16,
                            choices=CHOICES_ROLES
                            )
    name = models.CharField(max_length=128)
    birth_year = models.IntegerField(validators=[MinValueValidator(1900),
                                                 MaxValueValidator(current_date)
                                                 ]
                                     )

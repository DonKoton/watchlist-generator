from datetime import datetime

from django.db import models

from database import create_choices, get_max_votes_num
from functions import cur_date
from watchlist.validators import MaxValueValidator, MinValueValidator


class Movies(models.Model):
    CHOICES_GENRES = create_choices()
    CHOICES_GENRES.insert(0, ('', ''))

    movie_rating = models.FloatField(validators=[MinValueValidator(1.0),
                                           MaxValueValidator(10.0)
                                           ],
                               default='',
                               null=True
                               )
    movie_votes = models.IntegerField(validators=[MinValueValidator(1000),
                                            MaxValueValidator(get_max_votes_num())
                                            ],
                                blank=True,
                                null=True
                                )
    genre = models.CharField(max_length=32,
                             choices=CHOICES_GENRES,
                             blank=True,
                             null=True
                             )
    prod_year = models.IntegerField(validators=[MinValueValidator(1960),
                                                MaxValueValidator(cur_date())
                                                ],
                                    blank=True,
                                    null=True
                                    )
    number_of_movies_to_choose = models.IntegerField(validators=[MinValueValidator(1),
                                                                 MaxValueValidator(30)
                                                                 ]
                                                     )


class People(models.Model):
    CHOICES_ROLES = [
        ("actor", "Actor"),
        ("actress", "Actress"),
        ("director", "Director")
    ]
    CHOICES_ROLES.insert(0, ('', ''))
    current_date = datetime.today().year

    people_rating = models.FloatField(validators=[MinValueValidator(1.0),
                                           MaxValueValidator(10.0)
                                           ],
                               default='',
                               null=True
                               )
    people_votes = models.IntegerField(validators=[MinValueValidator(1000),
                                            MaxValueValidator(get_max_votes_num())
                                            ],
                                blank=True,
                                null=True
                                )
    role = models.CharField(max_length=16,
                            choices=CHOICES_ROLES,
                            null=True
                            )
    name = models.CharField(max_length=128, default='', blank=True, null=True)
    birth_year = models.IntegerField(validators=[MinValueValidator(1900),
                                                 MaxValueValidator(cur_date())
                                                 ],
                                     null=True
                                     )
    number_of_movies_to_choose = models.IntegerField(validators=[MinValueValidator(1),
                                                                 MaxValueValidator(30)
                                                                 ]
                                                     )

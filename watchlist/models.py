from django.db import models
from database import create_choices, get_max_votes_num
from watchlist.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Movies(models.Model):
    CHOICES_GENRES = create_choices()
    CHOICES_GENRES.insert(0, ('', ''))
    CHOICES_ROLES = [
        ("actor", "Actor"),
        ("actress", "Actress"),
        ("director", "Director")
    ]
    CHOICES_ROLES.insert(0, ('', ''))
    current_date = datetime.today().year

    rating = models.FloatField(validators=[MinValueValidator(1.0),
                                           MaxValueValidator(10.0)
                                           ],
                               default='',
                               null=True
                               )
    votes = models.IntegerField(validators=[MinValueValidator(1000),
                                            MaxValueValidator(get_max_votes_num())
                                            ],
                                blank=True,
                                null=True
                                )
    genre = models.CharField(max_length=32,
                             choices=CHOICES_GENRES,
                             default='',
                             blank=True,
                             null=True
                             )
    prod_year = models.IntegerField(validators=[MinValueValidator(1960),
                                                MaxValueValidator(current_date)
                                                ],
                                    default='',
                                    blank=True,
                                    null=True
                                    )
    role = models.CharField(max_length=16,
                            choices=CHOICES_ROLES,
                            default='',
                            blank=True,
                            null=True
                            )
    name = models.CharField(max_length=128, default='', blank=True, null=True)
    birth_year = models.IntegerField(validators=[MinValueValidator(1900),
                                                 MaxValueValidator(current_date)
                                                 ],
                                     default='',
                                     blank=True,
                                     null=True
                                     )
    number_of_movies_to_choose = models.IntegerField(validators=[MinValueValidator(1),
                                                                 MaxValueValidator(30)
                                                                 ]
                                                     )

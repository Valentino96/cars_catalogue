from django.db import models

from django.core import validators
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars_catalogue.cars.validators import min_len_validator, validate_year


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)],
        #validators=[min_len_validator],
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(18)],
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CARS = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER)
    )
    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CARS,
    )
    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[validators.MinLengthValidator(2)],
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[validate_year]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(1.0)],
    )



from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("NB", "Non_Binary"),
    )

    nickname = models.CharField(
        max_length=100,
        unique=True,
        error_messages={"unique": "A user with that nickname already exists."},
        default="",
    )
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)

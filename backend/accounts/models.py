# backend.accounts.models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

from . import managers

NULL_AND_BLANK = {'null': True, 'blank': True}


class CustomUser(AbstractUser):

    unsername = None
    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
    email= models.EmailField(
        verbose_name="email address",
        max_length=254, unique=True
    )
    bio = models.TextField(
        verbose_name="Your biography",
        **NULL_AND_BLANK
    )
    birth_date = models.DateField(
        verbose_name="birth date",
        **NULL_AND_BLANK
    )
    pro = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    class Meta:
        verbose_name_plural = 'accounts'

    def __str__(self):
        return f"{self.email}'s custom account"

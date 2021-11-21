from django.db import models

# Create your models here.
"""Models."""

from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountsUser(AbstractUser):
    """AccountsUser model."""

    AbstractUser._meta.get_field('username')._unique = False
    AbstractUser._meta.get_field('email')._unique = True

    ADMIN = 1
    CLIENT = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CLIENT, 'Client'),
        (EMPLOYEE, 'Employee'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


    def __str__(self) -> str:  # noqa: D105
        return self.email

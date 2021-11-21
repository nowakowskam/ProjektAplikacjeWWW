from django.db import models

# Create your models here.
"""Models."""

from django.db import models
from django.contrib.auth.models import AbstractUser


# class AccountsUser(AbstractUser):
#     """AccountsUser model."""
#
#     AbstractUser._meta.get_field('username')._unique = False
#     AbstractUser._meta.get_field('email')._unique = True
#
#     def __str__(self) -> str:  # noqa: D105
#         return self.email
#
#
# class Client(models.Model):
#     """Client model."""
#     phone_number = models.CharField(max_length=12, unique=True)
#     account = models.ForeignKey(AccountsUser, on_delete=models.PROTECT)
#
#     def __str__(self) -> str:  # noqa: D105
#         return f'{self.phone_number}:{self.account.email}'
#
#
# class Address(models.Model):
#     """Address model."""
#
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=20)
#     client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
#
# class Employee(models.Model):
#     account = models.ForeignKey(AccountsUser, on_delete=models.PROTECT)
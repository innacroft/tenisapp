from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    identification_number = models.CharField(
        max_length=20, unique=True, null=True,blank=True, verbose_name="Identification number")
    age = models.IntegerField(
        max_length=2, unique=False, null=True, blank=True, verbose_name="Age")
    
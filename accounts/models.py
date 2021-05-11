from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    id = models.AutoField(primary_key=True)

    phone = models.CharField(max_length=15, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    age = models.PositiveSmallIntegerField(blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    genderChoice = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length= 1, choices=genderChoice)
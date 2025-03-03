from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
      city = models.CharField(max_length=100)
      state_or_province = models.CharField(max_length=100)
      country = models.CharField(max_length=100)
      latitude = models.DecimalField(max_digits=9, decimal_places=6)
      longitude = models.DecimalField(max_digits=9, decimal_places=6)
      profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

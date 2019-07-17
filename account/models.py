from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True)
    time_table = models.CharField(default=('0' * 81), max_length=81)

from email.policy import default
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.get_username()

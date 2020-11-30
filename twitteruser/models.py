from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    display = models.CharField(max_length=100, null=True)

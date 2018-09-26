from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	tweet_counter = models.PositiveIntegerField(default=0)

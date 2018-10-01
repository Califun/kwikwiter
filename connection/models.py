from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    tweet_counter = models.PositiveIntegerField(default=0)
    like_counter = models.PositiveIntegerField(default=0)
    comment_counter = models.PositiveIntegerField(default=0)

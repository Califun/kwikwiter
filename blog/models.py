from django.db import models

from connection.models import User


class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	text = models.CharField(default="", max_length=1024)
	likes = models.ManyToManyField(User, related_name="posts_like")
	like_counter = models.PositiveIntegerField(default=0)

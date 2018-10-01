# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from django.db import IntegrityError, transaction
from django.db.models import F


from .models import Post
from public.utils import json_error_handler


@login_required
def home(request):
	posts = Post.objects.all().order_by("-created_at")
	likes = request.user.posts_like.all()

	return render(request, "blog/home.html", {"posts": posts, "likes": likes})


@login_required
@require_POST
def add_post(request):
	try:
		with transaction.atomic():
			post = Post()
			post.text = request.POST.get('add_post').strip()
			post.user = request.user
			post.save()
			request.user.tweet_counter = F('tweet_counter') + 1
			request.user.save()
			request.user.refresh_from_db()
	except IntegrityError:
		return json_error_handler("cant-save")

	return JsonResponse(
		{"success": True, "post_id": post.pk, "tweet_counter": request.user.tweet_counter})


def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Exception:
        return json_error_handler("cant-found")
    post.delete()
    request.user.tweet_counter = F('tweet_counter') - 1
    request.user.save()
    request.user.refresh_from_db()

    posts = Post.objects.all().order_by("-created_at")
    likes = request.user.posts_like.all()

    return render(request, "blog/home.html", {"posts": posts, "likes": likes})
    


@login_required
@require_GET
def like_post(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Exception:
		return json_error_handler("cant-found")
	try:
		with transaction.atomic():
			try:
				like = post.likes.get(pk=request.user.pk)
			except Exception:
				like = None
			if like:
				post.likes.remove(like)
				post.like_counter = F('like_counter') - 1
				post.save()
				result = True
			else:
				post.likes.add(request.user)
				post.like_counter = F('like_counter') + 1
				post.save()
				result = False
			post.refresh_from_db()
	except IntegrityError:
		return json_error_handler("cant-save")

	return JsonResponse({"success": True, "like": result, "like_counter": post.like_counter})

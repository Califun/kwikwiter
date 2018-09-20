# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse


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
		post = Post()
		post.text = request.POST.get('add_post').strip()
		post.user = request.user
		post.save()
	except Exception:
		return json_error_handler("cant-save")

	return JsonResponse({"success": True, "post_id": post.pk})


@login_required
@require_GET
def like_post(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Exception:
		return json_error_handler("cant-found")
	try:
		try:
			like = post.likes.get(pk=request.user.pk)
		except Exception:
			like = None

		if like:
			post.likes.remove(like)
			result = True
		else:
			post.likes.add(request.user)
			post.save()
			result = False

	except Exception:
		return json_error_handler("cant-save")
	return JsonResponse({"success": True, "like": result})

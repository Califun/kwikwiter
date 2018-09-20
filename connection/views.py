# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout


from public.utils import error_handler


def landing(request):
	if request.user.is_authenticated:
		return redirect("blog:home")
	return render(request, "connection/landing.html", {})


@require_POST
def log_in(request):
	username = request.POST.get("username")
	password = request.POST.get("password")
	if not username:
		return error_handler(request, "Please enter an username", redirect("connection:landing"))
	if not password:
		return error_handler(request, "Please enter a password", redirect("connection:landing"))

	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect("blog:home")
	else:
		return error_handler(request, "Username or password is incorrect", redirect("connection:landing"))


def log_out(request):
	logout(request)
	return redirect("connection:landing")

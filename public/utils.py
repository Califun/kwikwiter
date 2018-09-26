# -*- coding: utf-8 -*-

from django.contrib import messages
from django.http import JsonResponse


def error_handler(request, message, redirect):
	print(message)
	messages.error(request, message)
	return redirect


def json_error_handler(reason):
	return JsonResponse({"success": False, "reason": reason})

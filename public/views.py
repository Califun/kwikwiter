from django.shortcuts import render


def handler404(request):
	return render(request, 'public/404.html', {})

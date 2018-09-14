from django.conf.urls import url

from . import views

app_name = 'connection'
urlpatterns = [
	url(r'^$', views.landing, name='landing'),
]

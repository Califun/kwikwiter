from django.conf.urls import url

from . import views

app_name = 'connection'
urlpatterns = [
	url(r'^$', views.landing, name='landing'),
	url(r'^login\/?$', views.log_in, name='log_in'),
	url(r'^logout\/?$', views.log_out, name='log_out'),
]

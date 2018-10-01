from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^home\/?$', views.home, name='home'),
	url(r'^post/add\/?$', views.add_post, name='add_post'),
	url(r'^post/like/(?P<post_id>[0-9]+)\/?$', views.like_post, name='like_post'),
	url(r'^post/like/\/?$', views.like_post, name='like_post'),
	url(r'^delete/(?P<post_id>[0-9]+)\/?$', views.delete_post, name='delete_post'),
]

from django.conf.urls import include, url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from connection import views as connection

handler404 = 'public.views.handler404'
urlpatterns = [
	# url(r'^public/', include('public.urls')),
	# url(r'^blog/', include('blog.urls')),
	url(r'^connection/', include('connection.urls')),
	url(r'^blog/', include('blog.urls')),
	url(r'^$', connection.landing, name='landing'),

	url(
		r'^favicon.ico$',
		RedirectView.as_view(
			url=staticfiles_storage.url('public/img/favicon.ico'),
			permanent=True),
		name="favicon"
	),
]

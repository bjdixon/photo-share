from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^$', 'photo.views.list', name='list'),
		url(r'^(\d+)/$', 'photo.views.album', name='album'),
		url(r'^image/(\d+)/$', 'photo.views.image', name='image'),
)

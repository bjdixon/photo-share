from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'share_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'photo.views.main', name='main'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^photos/', include('photo.urls')),
)

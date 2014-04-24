from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from django.conf import settings

from photo.models import *

def home(request):
	return HttpResponse("Home")

def list(request):
	"""Main listing"""
	albums = Album.objects.all()
	if not request.user.is_authenticated():
		albums = albums.filter(public=True)

	paginator = Paginator(albums, 10)
	try: 
		page = int(request.GET.get("page", '1'))
	except ValueError: 
		page = 1

	try:
		albums = paginator.page(page)
	except (InvalidPage, EmptyPage):
		albums = paginator.page(paginator.num_pages)

	for album in albums.object_list:
		album.images = album.image_set.all()[:4]

	return render_to_response("list.html", dict(albums=albums, user=request.user, media_url=settings.MEDIA_URL))

def album(request, album_id):
	"""Album listing"""
	album = Album.objects.get(id=album_id)
	if not album.public and not request.user.is_authenticated():
		return HttpResponse("Error: you need to be logged in to view this album")

	images = album.image_set.all()
	paginator = Paginator(images, 30)
	try:
		page = int(request.GET.get("page", '1'))
	except ValueError:
		page = 1
	try:
		images = paginator.page(page)
	except (InvalidPage, EmptyPage):
		images = paginator.page(paginator.num_pages)
	return render_to_response('album.html', dict(album=album, images=images, media_url=settings.MEDIA_URL))
	
def image(request, image_id):
		"""Image page"""
		img = Image.objects.get(id=image_id)
		return render_to_response('image.html', dict(image=img, user=request.user, backurl=request.META["HTTP_REFERER"], media_url=settings.MEDIA_URL))


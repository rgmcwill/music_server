from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from .models import Song, Playlist
from .forms import UserForm

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
	if not request.user.is_authenticated:
		return render(request, 'login.html')
	else:
		#Will query here
		#albums = Album.objects.filter(user=request.user)
		song_results = Song.objects.all()
		query = request.GET.get("q")
		if query:
			print('A query was sent, and it was : ', query)
			return render(request, 'index.html', {})
			'''albums = albums.filter(
				Q(album_title__icontains=query) |
				Q(artist__icontains=query)
			).distinct()
			song_results = song_results.filter(
				Q(song_title__icontains=query)
			).distinct()
			return render(request, 'index.html', {
				'albums': albums,
				'songs': song_results,
			})'''
		else:
			return render(request, 'index.html', {})

def register(request):

	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				#albums = Album.objects.filter(user=request.user)
				return render(request, 'index.html', {})
	context = {
		"form": form,
	}
	return render(request, 'register.html', context)

def login_user(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
		  if user.is_active:
			  login(request, user)
			  #albums = Album.objects.filter(user=request.user)
			  return render(request,'index.html',{})
		  else:
			  return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'login.html', {'error_message': 'Invalid login'})
	return render(request, 'login.html')

def logout_user(request):

	logout(request)
	form = UserForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, 'login.html', context)

def songs(request):
	return render(request, 'login.html')

def create_playlist(request):
	return render(request, 'login.html')
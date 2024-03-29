from django.conf.urls import url

from . import views

app_name = 'music'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^create_playlist/$', views.create_playlist, name='create_playlist'),
	url(r'^update_songs/$', views.update_songs, name='update_songs'),
]

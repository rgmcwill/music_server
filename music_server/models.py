from django.db import models

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    audio_file = models.FileField(default='')

    def __str__(self):
        return self.song_name

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlist_name

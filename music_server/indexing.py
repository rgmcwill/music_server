import os, audio_metadata
from .dbSong import DB_Song_Interface

def rec_music_index(path):
	dir = []
	print('-----Current Path ('+ path +')-----')
	print('Files:')
	for i in os.listdir(path):
		if not os.path.isdir(path+i):
			meta_test(path+i)
			#print(i)
		else:
			dir.append(i)
	print('Folders:')
	for i in dir:
		print(i)
		rec_music_index(path+i+'/')

def meta_test(path):
	am = audio_metadata.load(path)
	print('path: '+ path.replace('media/','') + ' | name: ' + am.tags.get('title')[0])
	db = DB_Song_Interface
	db.create_single_song(db,am.tags.get('title')[0], path.replace('media/',''))
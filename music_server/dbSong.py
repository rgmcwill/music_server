from django.utils import timezone
from django.db.models import Q
from .models import Song

class DB_Song_Interface:
    def __init__(self):
        self.s = None

    def get_by_song_name(self,song_name):
        return Song.objects.filter(song_name=song_name)

    def get_by_audio_file(self,audio_file):
        return Song.objects.filter(audio_file=audio_file)

    def get_all_songs(self):
        return Song.objects.all()

    def create_single_song(self,song_name,audio_file):
        print(song_name)
        print(audio_file)
        self._add_to_db(self,song_name,audio_file,False)

    '''def create_games_from_list(self,game_list):
        #will follow the structure of [game{"team name":score,"team_name",score},game{"team name":score,"team_name",score}]
        for i in range(len(game_list)):
            dict = game_list[i]
            team1 = list(dict.keys())[0]
            team2 = list(dict.keys())[1]
            score1 = dict.get(team1)
            score2 = dict.get(team2)
            date_start_time = dict.get("date_start_time")

            print(team1 + "|" + score1 + "|" + team2 + "|" + score2)

            self._add_to_db(team1,team2,score1,score2,date_start_time,False)'''

    def _add_to_db(self,song_name,audio_file,override):
        if not override:
            if not Song.objects.filter(song_name=song_name,audio_file=audio_file).exists():
                self.s = Song(song_name=song_name,audio_file=audio_file)
                self.s.save()
        else:
            self.s = Song(song_name=song_name,audio_file=audio_file)
            self.s.save()

    def clear_table(self):
        for i in Song.objects.all():
            i.delete()

# Generated by Django 2.2.5 on 2019-10-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_server', '0003_song_song_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_path',
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
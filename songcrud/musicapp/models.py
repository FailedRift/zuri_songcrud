from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

class Song(models.Model):
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    released_date = models.DateField()

class Lyrics(models.Model):
    content = models.CharField(max_length=2000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

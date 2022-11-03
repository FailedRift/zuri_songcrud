from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    released_date = models.DateField()

    def __str__(self):
        return self.title
        
class Lyrics(models.Model):
    content = models.CharField(max_length=2000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

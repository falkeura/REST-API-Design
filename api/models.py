from django.db import models

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()
    #albums = models.ManyToManyField(to=Album)
    def __str__(self):
        return self.name

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    duration = models.IntegerField()
    artists = models.ManyToManyField(to=Artist)
    def __str__(self):
        return self.name

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(to=Artist)
    name = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()
    tracks = models.ManyToManyField(to=Track)
    def __str__(self):
        return self.name



from rest_framework import serializers
from api.models import Track, Artist, Album

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    artistslist = serializers.HyperlinkedIdentityField(view_name='track-artists', format='html')

    class Meta:
        model = Track
        fields = ('url','id', 'name', 'duration','artists', 'artistslist')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albumslist = serializers.HyperlinkedIdentityField(view_name='artist-listall', format='html')

    class Meta:
        model = Artist
        fields = ('url','id', 'name', 'year', 'albumslist')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    trackslist = serializers.HyperlinkedIdentityField(view_name='album-listall', format='html')

    class Meta:
        model = Album
        fields = ('url','id','name','year','tracks','artist','trackslist')
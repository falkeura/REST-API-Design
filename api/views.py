from django.shortcuts import render

# Create your views here.
from api.models import Track, Artist, Album
from api.serializers import TrackSerializer, ArtistSerializer, AlbumSerializer
from rest_framework import viewsets,permissions
from rest_framework.decorators import detail_route,renderer_classes, api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

class TrackSearch(APIView):

    def get(self, request, query, format=None):
        tracks = Track.objects.filter(name__contains=query)
        serializer = TrackSerializer(tracks, many=True, context={'request':request})
        return Response(serializer.data)

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save()

    @detail_route(methods=['get'], permission_classes=[])
    @renderer_classes((TemplateHTMLRenderer,))
    def artists(self, request, pk):
        track = Track.objects.get(id=pk)
        artists = track.artists.all()
        ser = ArtistSerializer(artists, many=True, context={'request':request})
        return Response(ser.data)

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.AllowAny,)

    @detail_route(methods=['get'], permission_classes=[])
    @renderer_classes((TemplateHTMLRenderer,))
    def listall(self, request, pk):
        artist = Artist.objects.get(id=pk)
        album = Track.objects.filter(artists=artist)
        ser = TrackSerializer(album, many=True, context={'request':request})
        return Response(ser.data)

    def perform_create(self, serializer):
        serializer.save()


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.AllowAny,)

    @detail_route(methods=['get'], permission_classes=[])
    @renderer_classes((TemplateHTMLRenderer,))
    def listall(self, request, pk):
        album = Album.objects.get(id=pk)
        track = album.tracks.all()
        ser = TrackSerializer(track, many=True, context={'request':request})
        return Response(ser.data)

    def perform_create(self, serializer):
        serializer.save()


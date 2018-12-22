# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, views
from providers.songspk import SongsPK
from models import Album, Track
from serializers import AlbumSerializer, TrackSerializer

@api_view(['POST'])
def search(request):
	search_type = request.data.get('search_type', None)
	q = request.data.get('q', None)
	if q and search_type:
		if search_type == 'album':
			data = SongsPK().search_for_albums(q)
			return Response(data)
	return Response(data={'message': 'please provide correct input'}, status=400)

@api_view(['POST'])
def fetch_album_details(request):
	url = request.data.get('url', None)
	if url:
		data = SongsPK().fetch_album_details(url)
		return Response(data)
	return Response(data={'message': 'please provide correct input'}, status=400)

class TrackViewSet(viewsets.ModelViewSet):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer

class AlbumViewSet(viewsets.ModelViewSet):

	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

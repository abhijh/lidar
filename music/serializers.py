import os, uuid, requests
from django.conf import settings
from rest_framework import serializers
from models import Album, Track
import urllib, tempfile

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'url', 'image', 'pid', 'tracks')

    # def validate_image(self, attrs):
        # print "hello"
        # image_url = attrs['image']
        # response = requests.get(image_url)
        # random_name = attrs['title'] + image_url.split('.')[-1]
        # folder_name = "albums/" + attrs['title']
        # absolute_file_path = os.path.join(settings.MEDIA_ROOT, folder_name, random_name)
        # relative_path = os.path.join(folder_name, random_name)
        # with open(absolute_file_path, 'wb') as f:
        #     f.write(response.content)
        # attrs['image'] = relative_path
        # return attrs
        # 
        # 2nd method
        # 
        # URL = attrs['image']
        # img_temp = tempfile.NamedTemporaryFile(delete=True)
        # img_temp.write(urllib.urlopen(URL).read())
        # img_temp.flush()

        # attrs['image'] = img_temp
        # return attrs

    def create(self, validated_data):
        track_list = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track in track_list:
            Track.objects.create(album=album, **track)
        return album
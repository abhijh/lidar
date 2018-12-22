# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Album, Track

admin.site.register(Track)


class TrackInline(admin.StackedInline):
    model = Track


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline, ]
    list_display = ['title', 'track_count']

    def track_count(self, instance):
        return instance.tracks.count()
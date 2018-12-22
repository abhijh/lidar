# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    # released = models.CharField(max_length=100)
    # artist = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    image = models.ImageField(blank=True)
    pid = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.title

class Track(models.Model):

    STATUS_CHOICES = (
        ('Q', 'QUEUED'),
        ('D', 'DOWNLOADED'),
        ('S', 'SKIPPED'),
    )

    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE, blank=True)
    path = models.CharField(max_length=1000, null=True, blank=True)
    url = models.URLField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='S',
    )

    def __unicode__(self):
        return self.title

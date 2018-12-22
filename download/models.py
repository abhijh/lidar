# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
    AUTH_TYPE_CHOICES = (
        ('B', 'BASIC'),
        ('P', 'POST PARAM'),
        ('H', 'HEADER'),
        ('C', 'COOKIE'),
    )
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    auth_required = models.BooleanField(default=False, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    auth_type = models.CharField(
        max_length=2,
        choices=AUTH_TYPE_CHOICES,
        default='B',
    )
    token_key = models.CharField(max_length=100, null=True, blank=True)
    list_endpoint = models.CharField(max_length=100, null=True, blank=True)
    status_endpoint = models.CharField(max_length=100, null=True, blank=True)
    add_endpoint = models.CharField(max_length=100, null=True, blank=True)
    delete_endpoint = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s:%s" % (self.host, self.port)

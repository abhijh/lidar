# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-16 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20181216_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='task_id',
        ),
    ]

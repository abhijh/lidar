# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-16 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0003_auto_20181216_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]

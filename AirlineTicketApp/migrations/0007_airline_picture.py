# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineTicketApp', '0006_auto_20171018_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='picture',
            field=models.URLField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineTicketApp', '0008_auto_20171018_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineTicketApp', '0004_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='from_location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='to_location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineTicketApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plane',
            name='numbers_of_seats_3',
            field=models.IntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineTicketApp', '0007_airline_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='picture',
            field=models.FileField(null=True, upload_to='images/airline-logo/'),
        ),
    ]

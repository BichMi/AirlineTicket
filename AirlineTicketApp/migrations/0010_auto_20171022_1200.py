# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineTicketApp', '0009_bookinfo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='from_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_location', to='AirlineTicketApp.Location'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='to_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_location', to='AirlineTicketApp.Location'),
        ),
    ]

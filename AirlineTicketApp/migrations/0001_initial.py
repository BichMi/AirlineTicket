# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 03:48
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=50)),
                ('airline_price', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=100)),
                ('airport_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_book_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('seat_number', models.IntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=100)),
                ('to_location', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField(blank=True, null=True)),
                ('flight_time', models.TimeField()),
                ('time_to_airport_mid', models.TimeField(null=True)),
                ('time_from_airport_mid', models.TimeField(null=True)),
                ('airport_mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='FlightRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_route_name', models.CharField(max_length=255)),
                ('distance', models.IntegerField()),
                ('from_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_airport', to='AirlineTicketApp.Airport')),
                ('to_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_airport', to='AirlineTicketApp.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planes_name', models.CharField(max_length=50, null=True)),
                ('manufacturer', models.CharField(max_length=100, null=True)),
                ('numbers_of_seats_1', models.IntegerField(null=True)),
                ('numbers_of_seats_2', models.IntegerField(null=True)),
                ('payload_allowed', models.IntegerField(null=True)),
                ('gate_number', models.IntegerField(null=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='SeatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_class_name', models.SmallIntegerField(choices=[(0, 'Econnomy'), (1, 'Premium Economy'), (2, 'Business')])),
                ('seat_class_price', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.Flight')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type_name', models.SmallIntegerField(choices=[(0, 'Adults'), (1, 'Childrent'), (2, 'Baby')])),
                ('ticket_type_price', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(null=True)),
                ('sex', models.CharField(max_length=20, null=True)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('certificate_of_identity_card', models.IntegerField(null=True)),
                ('contact_telephone', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('user_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.UserType')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='ticketbook',
            name='user',
            field=models.ForeignKey(help_text='Khách Hàng', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.FlightRoute'),
        ),
        migrations.AddField(
            model_name='flight',
            name='planes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.Plane'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.TicketBook'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='seat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.SeatType'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='ticket_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AirlineTicketApp.TicketType'),
        ),
    ]

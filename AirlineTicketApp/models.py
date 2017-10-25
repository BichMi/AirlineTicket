from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from AirlineTicket import settings

class UserType(models.Model):
    user_type_name = models.CharField(max_length=50)

    def __str__(self):
        return ("%s - %s" % (self.pk, self.user_type_name))

class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    sex = models.CharField(max_length=20, null=True)
    nationality = models.CharField(max_length=100, null=True)
    certificate_of_identity_card = models.CharField(max_length=50, null=True)
    contact_telephone = models.CharField(max_length=20, null=True)
    user_type = models.ForeignKey(UserType, default=1)
    def __str__(self):
        return ("%s - User Name:%s - Ho va Ten: %s %s - Birthday: %s - Gioi Tinh: %s - Quoc Tich: %s - Email: %s -CMND: %r - Loai User:%s" % (
            self.pk, self.username, self.last_name, self.first_name, self.date_of_birth, self.sex,self.nationality, self.email,
            self.certificate_of_identity_card, self.user_type_id))

class SeatType(models.Model):
    seat_class_name = models.CharField(max_length=100, null=True)
    seat_class_price = models.FloatField(null=True, blank=True, default=0.00)

    def __str__(self):
        return ("%s - %s - %f" % (self.pk, self.seat_class_name, self.seat_class_price))

class Airport(models.Model):
    airport_name = models.CharField(max_length=100)
    airport_address = models.CharField(max_length=200)
    def __str__(self):
        return ("%s - %s - %s" % (self.pk, self.airport_name, self.airport_address))

class TicketType(models.Model):
    ADULTS, CHILDREN, BABY = range(3)
    TYPETICKET = ((ADULTS, "Adults"), (CHILDREN, "Childrent"), (BABY, "Baby"))
    ticket_type_name = models.SmallIntegerField(choices=TYPETICKET)
    ticket_type_price = models.FloatField(null=True, blank=True, default=0.00)
    def __str__(self):
        return ("%s - %d - %f" % (self.pk, self.ticket_type_name, self.ticket_type_price))

class Airline(models.Model):
    airline_name = models.CharField(max_length=50)
    airline_price = models.FloatField(null=True, blank=True, default=0.00)
    picture = models.FileField(upload_to='images/airline-logo/', null=True)
    def __str__(self):
        return ("%s - %s - %f " % (self.pk, self.airline_name, self.airline_price))

class Plane(models.Model):
    planes_name = models.CharField(max_length=50, null=True)
    airline = models.ForeignKey(Airline)
    manufacturer = models.CharField(max_length=100, null=True)
    numbers_of_seats_1 = models.IntegerField(null=True)
    numbers_of_seats_2 = models.IntegerField(null=True)
    numbers_of_seats_3 = models.IntegerField(null=True)
    payload_allowed = models.IntegerField(null=True)
    gate_number = models.IntegerField(null=True)
    def __str__(self):
        return ("%s - %s - %s - %s - %d - %d - %d - %d - %d" % (
            self.pk, self.planes_name, self.airline, self.manufacturer, self.numbers_of_seats_1,
            self.numbers_of_seats_2, self.numbers_of_seats_3, self.payload_allowed, self.gate_number))

class FlightRoute(models.Model):
    flight_route_name = models.CharField(max_length=255)
    from_airport = models.ForeignKey(Airport, related_name='from_airport')
    to_airport = models.ForeignKey(Airport, related_name='to_airport')
    distance = models.IntegerField()
    def __str__(self):
        return (
            "%s - %s - %s - %s - %d" % (
            self.pk, self.flight_route_name, self.from_airport, self.to_airport, self.distance))

class Location(models.Model):
    location_name = models.CharField(max_length=255, null=True)
    def __str__(self):
        return ("%s" % (self.location_name))

class Flight(models.Model):
    flight_route = models.ForeignKey(FlightRoute)
    planes = models.ForeignKey(Plane)
    from_location = models.ForeignKey(Location, related_name='from_location', null=True)
    to_location = models.ForeignKey(Location, related_name='to_location', null=True)
    departure_day = models.DateField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    arrive_day = models.DateField(null=True, blank=True)
    flight_time = models.TimeField(null=True)
    arrive_time = models.TimeField(null=True)
    airport_mid = models.ForeignKey(Airport, null=True)
    time_to_airport_mid = models.TimeField(null=True)
    time_from_airport_mid = models.TimeField(null=True)
    def __str__(self):
        return ("%s - %s - %s - %s -%s - %s -%s -%s - %s - %s - %s" % (
            self.pk, self.from_location, self.to_location,self.departure_day, self.departure_time, self.arrive_day, self.arrive_time,self.flight_time, self.airport_mid,
            self.time_to_airport_mid, self.time_from_airport_mid))

class BookInfo(models.Model):
    flight = models.ForeignKey(Flight, null=True)
    seat_type = models.ForeignKey(SeatType)
    ticket_type = models.ForeignKey(TicketType)
    ticket_book_price = models.FloatField(null=True, blank=True, default=0.0)
    airline = models.ForeignKey(Airline)
    seat_number = models.IntegerField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return ("%s -%f - %d - %s - %s" % (self.pk, self.ticket_book_price, self.seat_number, self.status, self.airline.airline_name))

class TicketBook(models.Model):
    user = models.ForeignKey(User, help_text='Khách Hàng')
    book_info = models.ForeignKey(BookInfo, related_name='book_info', null=True)
    def __str__(self):
        return ("%s - ID User book: %s - ID Flight: %s" % (
            self.pk, self.user_id, self.book_info))

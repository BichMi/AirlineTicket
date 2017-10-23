from .models import *


def get_common_data():
    seat_type = SeatType.objects.all()
    location = Location.objects.all()
    airline = Airline.objects.all()
    ticket_book = TicketBook.objects.all()
    book_info = BookInfo.objects.filter()


    return {
        "seat_type": seat_type,
        "location": location,
        "airline": airline,
        "ticket_book": ticket_book,
        "book_info": book_info,
    }
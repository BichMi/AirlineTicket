from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseNotFound
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, TicketBookForm, FlightForm, BookInfoForm, Airline
from .models import UserType, User, TicketBook, BookInfo, Airline, SeatType, Location, Flight, FlightRoute, TicketType
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .services import get_common_data


def index(request):
   data = get_common_data()
   login_form = LoginForm()
   register_form = RegisterForm()
   book_info_form = BookInfoForm()
   ticket_book_form = TicketBook()

   context = {
       "register_form": register_form,
       "login_form": login_form,
       "book_info_form": book_info_form,
       "ticket_book_form": ticket_book_form
   }

   context.update(data)

   return render(request, 'AirlineTicketApp/index.html', context)


def login_view(request):
    login_form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)

            return redirect(reverse("home"))

    return render(request, 'index.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect(reverse("home"))


def register_user_view(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect(reverse("home"))

    return render(request, "home", {'register_form': form})

#đặt vé   kiểm tra bắt buộc đăng nhập
@login_required
def ticket_book_view(request):
    context_data = {}
    if request.method == "POST":
        ticket_book_form = TicketBookForm(data=request.POST, user=request.user)
        ticket_book_form.user = request.user

        if ticket_book_form.is_valid():
            ticket_book_form.save()

            return render("book_info", 'dat-ve.html')
    elif request.method == "GET":
        #EX request.GET: <QueryDict: {'LocationFrom': ['Đà Nẵng'], 'LocationTo': ['Phú Quốc'], 'SeatType': ['2'], 'AdultNo': ['3'], 'ChildrenNo': ['4'], 'BabyNo': ['1']}>
        import json
        context_data = json.loads(json.dumps(request.GET))

        info = BookInfo.objects.select_related().all()

        context_data = {
            "ticket":context_data,
            "info": info
        }

    return render(request, 'dat-ve.html', context_data)


@transaction.atomic
def book_info_view(request, ticket_book_id):
    context_data = {}
    book_info_form = BookInfoForm(request.POST)
    if request.method == "POST":
        book_info_form = BookInfoForm(data=request.POST,  book=BookInfo.objects.get(pk=ticket_book_id))
        book_info_form.book = request.book

        if book_info_form.is_valid():
            book_info_form.save()

            return redirect(reverse(request, kwargs={"ticket_book_id": ticket_book_id}))

    return render(request, "dat-ve.html",context_data, {"book_info_form": book_info_form})
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseNotFound
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def index(request):
    login_form = LoginForm()
    return render(request, 'AirlineTicketApp/index.html', {"login_form": login_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)

            return redirect(reverse("home"))

    return HttpResponseNotFound()


def logout_view(request):
    logout(request)
    return redirect(reverse("home"))
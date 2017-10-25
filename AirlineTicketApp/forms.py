from django import forms
from django.forms import PasswordInput

from AirlineTicket import settings
from AirlineTicketApp.models import User, UserType, TicketBook, BookInfo, Flight, Airline, Location


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tài khoản", "required": True}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Mật khẩu", "required": True})
        }

class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nhập tên", "required": True}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nhập họ", "required": True}))
    email = forms.EmailField(required=True,  widget= forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "required": True}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={"class": "form-control", "placeholder": "Ngày sinh", "required": True}))
    sex = forms.CharField(required=True, widget= forms.TextInput(attrs={"class": "form-control", "placeholder": "Giới tính", "required": True}))
    nationality = forms.CharField(required=True,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Quốc tịch", "required": True}) )
    certificate_of_identity_card = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Chứng minh thư", "required": True}))
    contact_telephone = forms.CharField(required=True,widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Số điện thoại", "required": True}) )
    confirm_password = forms.CharField(max_length=20, widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Nhâp lại mật khẩu", "required": True}))
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email","confirm_password", "date_of_birth", "sex", "nationality", "certificate_of_identity_card", "contact_telephone", "password")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tài khoản", "required": True}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nhập tên", "required": True}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nhập họ", "required": True}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "required": True}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "placeholder": "Ngày sinh", "required": True}),
            "sex": forms.TextInput(attrs={"class": "form-control", "placeholder": "Giới tính", "required": True}),
            "nationality": forms.TextInput(attrs={"class": "form-control", "placeholder": "Quốc tịch", "required": True}),
            "certificate_of_identity_card": forms.TextInput(attrs={"class": "form-control", "placeholder": "Chứng minh thư", "required": True}),
            "contact_telephone": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Số điện thoại", "required": True}),
            "password": PasswordInput(attrs={"class": "form-control", "placeholder": "Mật khẩu", "required": True}),
            "confirm_password": PasswordInput(attrs={"class": "form-control", "placeholder": "Nhập lại mật khẩu", "required": True}),
        }

    # Ghi đè phương thức kiểm tra input
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")
        if not confirm_password == password:
            self.add_error("password", "Passwords không khớp!")

    def save(self):
        user = super().save()
        user.set_password(self.cleaned_data["password"])
        user.save()

        return user

# đặt vé
class TicketBookForm(forms.ModelForm):
    class Meta:
        model = TicketBook
        fields = ()

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("user", "")
        self.book_info = kwargs.pop("book_info", "")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.current_user
        self.instance.book_info = self.book_info

        return super().save(commit=commit)


class BookInfoForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = ("ticket_book_price","seat_number", "status")

    def __init__(self, *args, **kwargs):
        self.flight = kwargs.pop("flight", "")
        self.seat_type = kwargs.pop("seat_type", "")
        self.ticket_type = kwargs.pop("ticket_type", "")
        self.airline = kwargs.pop("airline", "")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.current_user
        self.instance.flight = self.flight
        self.instance.seat_type = self.seat_type
        self.instance.ticket_type = self.ticket_type
        self.instance.airline = self.airline

        return super().save(commit=commit)


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ("departure_day", "departure_time", "flight_time", "airport_mid","time_to_airport_mid", "time_from_airport_mid")


    def __init__(self, *args, **kwargs):
        self.from_location =  kwargs.pop("from_location", "")
        self.to_location = kwargs.pop("to_location", "")
        self.flight_route = kwargs.pop("flight_route", "")
        self.planes = kwargs.pop("planes", "")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.location = self.from_location
        self.instance.location = self.to_location
        self.instance.flight_route = self.flight_route
        self.instance.planes = self.planes

        return super().save(commit=commit)



class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ("airline_name","picture")

    def __init__(self):
        super().__init__()

    def save(self, commit=True):
        return super().save(commit=commit)

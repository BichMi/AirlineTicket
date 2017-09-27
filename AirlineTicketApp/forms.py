from django import forms
from AirlineTicketApp.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tài khoản", "required": True}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Mật khẩu", "required": True})
        }
# Django imports
from django import forms


class UserRegisterForm(forms.Form):
    """
        Creates User registration form for signing up.
    """

    first_name = forms.CharField(widget=forms.TextInput(attrs={
            "name": "first_name", "class": "form-control form-control-user",
            "placeholder": "Enter First Name..."
        }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
            "name": "last_name", "class": "form-control form-control-user",
            "placeholder": "Enter Last name..."
        }))

    username = forms.CharField(widget=forms.TextInput(attrs={
            "name": "username", "class": "form-control form-control-user",
            "placeholder": "Enter Username..."
        }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
            "name": "email", "class": "form-control form-control-user",
            "placeholder": "Enter Email..."
        }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "name": "password",  "class": "form-control form-control-user",
            "placeholder": "Enter Password..."
        }))


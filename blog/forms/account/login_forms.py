# Django imports
from django import forms


class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
            "name": "username", "class": "form-control form-control-user",
            "placeholder": "Enter Username..."
        }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "name": "password",  "class": "form-control form-control-user",
            "placeholder": "Enter Password..."
        }))
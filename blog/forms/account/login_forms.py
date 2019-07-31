# Django imports
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    """
        Form for logging user in.
    """

    def __int__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        username = forms.EmailField(widget=forms.TextInput(attrs={
            "name": "username", "class": "form-control form-control-user",
            "placeholder": "Enter Username..."
        }))
        password = forms.CharField(widget=forms.PasswordInput(attrs={
            "name": "password",  "class": "form-control form-control-user",
            "placeholder": "Enter Password..."
        }))

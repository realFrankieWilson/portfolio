""" Moduls provide the logic for user's login details."""

from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class signUp(UserCreationForm):
    """
        Creates a signup form interface for user.
        attributes ->
            email:  Provides an email field(from django forms module)
            Meta:   Prepares user fields for modifications.
    """
    email = forms.EmailField()

    class Meta:
        """
            Creates a field for login details
            fields contians ->
                username:   user's username.
                email:  user's email
                password1: user's password
                password2:  user's password verification
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args: Any, **kwargs):
        super(signUp, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

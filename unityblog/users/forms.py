""" Moduls provide the logic for user's login details."""

from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


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
        """Removes the help text from the form"""
        super(signUp, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):
    """Edits users form"""
    class Meta:
        model = User
        fields = [
            'username', 'email',
        ]
    def __init__(self, *args: Any, **kwargs):
        """Removes the help text from form"""
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email',]:
            self.fields[fieldname].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    """Updates user profile"""
    class Meta:
        model = UserProfile
        fields = [
            'image'
        ]
    
    
    





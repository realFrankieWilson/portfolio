"""Contains the form for letting users make post via the user interface."""
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """A sub class that inherits from the modelform class"""
    class Meta:
        """
            attributes ->
                model: contains the post objects
                fields: some accessible fields.
        """
        model = Post
        fields = ('title', 'content')
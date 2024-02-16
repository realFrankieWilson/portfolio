"""Contains the form for letting users make post via the user interface."""
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """A sub class that inherits from the modelform class"""
    content = forms.CharField(widget=forms.TextInput(attrs={'rows': 4}))
    class Meta:
        """
            attributes ->
                model: contains the post objects
                fields: some accessible fields.
        """
        model = Post
        fields = ('title', 'content')


class PostUpdateForm(forms.ModelForm):
    """ Inherits from forms.ModelsForm"""
    class Meta:
        model = Post
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    """A Comment form class"""
    content = forms.CharField(
        label='', widget=forms.Textarea(attrs={'placeholder': 'Add comment'})
    )
    class Meta:
        model = Comment
        fields = ('content',)
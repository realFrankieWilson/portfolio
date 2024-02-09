"""
    Contains business logic of blog
    Logic include:
        Reading from database.
        Writing to database.
        Deleting from database
        Updating in a database and
        Shows data to the website
"""
from django.shortcuts import render
from .models import Post


def index(request):
    """Shows contents to the webpage"""
    posts = Post.objects.all()  # django ORM

    return render(request, 'blog/index.html', {'posts': posts})

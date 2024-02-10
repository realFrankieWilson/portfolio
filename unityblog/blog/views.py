"""
    Contains business logic of blog
    Logic include:
        Reading from database.
        Writing to database.
        Deleting from database
        Updating in a database and
        Shows data to the website
"""
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    """
        Shows contents to the webpage,
        get a post and stores it to the data base
    """
    posts = Post.objects.all()  # django ORM

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            isinstance = form.save(commit=False)
            isinstance.author = request.user
            isinstance.save()
            return redirect('blog-index')
    else:
        form = PostForm()
   
    context = {
        'posts': posts,
        'form': form
    }


    return render(request, 'blog/index.html', context)

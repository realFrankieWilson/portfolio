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
from .forms import PostForm, PostUpdateForm

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


def post_detail(request, pk):
    """Returns A post's detail"""
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

def post_edit(request, pk):
    """Returns Edit page template."""
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
    """Deletes a post """
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post,
    }
    return render(request, 'blog/post_delete.html', context)

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
from .forms import PostForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


@login_required
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


@login_required
def post_detail(request, pk):
    """Returns A post's detail"""
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        com_form = CommentForm(request.POST)
        if com_form.is_valid():
            instance = com_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        com_form = CommentForm()
    context = {
        'post': post,
        'com_form': com_form,
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
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

login_required
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

# def send_mail(request):
#     if request.method == 'POST':
#         message = request.POST['message']
#         email = request.POST['email']
#         name = request.POST['name']
#         send_mail(
#             'Contact form',
#             message,
#             'settings.EMAIL_HOST_USER',
#             ['frankuwill101@gmail.com'],
#             fail_silently=False
#         )
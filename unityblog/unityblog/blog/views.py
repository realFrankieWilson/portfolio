"""contains business logic of blog"""
from django.shortcuts import render


def index(request):
    """"""
    return render(request, 'blog/index.html')

from django.shortcuts import render

# Create your views here.
def frontpage(request):
    """A function that returns an html page from template folder"""
    return render(request, 'core/base.html')
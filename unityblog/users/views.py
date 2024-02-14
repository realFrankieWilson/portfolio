from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import signUp

# Create your views here.
def signup(request):
    """
        Renders the form page for signup and if succesful,
        Redirects users to home page
    """
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = signUp()
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)

def logout_view(request):
    """A customised logout page"""
    logout(request)
    return render(request, 'users/logout.html')

def profile(request):
    """
        Returns a profile page
    """
    return render(request, 'users/profile.html')
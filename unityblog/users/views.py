from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import signUp, UserUpdateForm, ProfileUpdateForm

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
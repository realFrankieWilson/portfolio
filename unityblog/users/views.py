from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import signUp

# Create your views here.
def signup(request):
    """Renders the form page for signup"""
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form = signUp()
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')
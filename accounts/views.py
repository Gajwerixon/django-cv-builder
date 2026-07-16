from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegisterForm


def register_view(request):
    """Create register view"""

    # user send data
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = RegisterForm()
    
    return render(
        request, 
        'accounts/register.html',
        {
             'form': form,         
        },
    )


def login_view(request):
    """Login user"""

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'accounts/login.html')
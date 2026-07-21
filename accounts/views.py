from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm


def register_view(request):
    """Create register view"""

    # user send data
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    
        if form.is_valid():
            
            user = form.save()
            login(request, user)

            # Redirect to the dashboard after successful registration
            return redirect("dashboard")
    
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
            return redirect('dashboard')
        
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect("/")
from django.shortcuts import render

# Create your views here => web logic (links to templates)
# request => object containing information about user's query
# (who entered; method (GET/POST), what data user's send) 
# render => combain Python and HTML

def home(request):
    """Home page"""
    return render(request, 'home.html')
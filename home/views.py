from django.shortcuts import render

def index(request):
    """View to render the home index page"""
    return render(request, 'home/index.html')

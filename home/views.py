from django.shortcuts import render


def index(request):
    """
    A view to show the store homepage
    """
    return render(request, 'home/index.html')

def about_us(request):
    """
    A view to display the about us page
    """
    return render(request, 'home/about.html')
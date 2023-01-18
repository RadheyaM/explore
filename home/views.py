from django.shortcuts import render


def index(request):
    """
    A view to show the store homepage
    """
    template = 'home/index.html'
    return render(request, template)

def about_us(request):
    """
    A view to display the about us page
    """
    template = 'home/about.html'
    return render(request, template)
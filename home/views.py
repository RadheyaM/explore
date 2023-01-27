from django.shortcuts import render, get_object_or_404
from products.models import Books


def index(request):
    """
    A view to show the store homepage
    """

    feature = get_object_or_404(Books, code='BHM9-XWP5-B48C-EKPB')

    return render(request, 'home/index.html', {'book': feature})

def about_us(request):
    """
    A view to display the about us page
    """
    return render(request, 'home/about.html')
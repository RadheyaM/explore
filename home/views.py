from django.shortcuts import render


def index(request):
    """
    A view to show the store homepage
    """
    return render(request, 'home/index.html')

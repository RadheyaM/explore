from django.shortcuts import render


def books(request):
    """
    A view to show all book products available for sale.
    """
    return render(request, 'products/books.html')

from django.shortcuts import render
from .models import Books


def books(request):
    """
    A view to show all book products available for sale.
    """
    books = Books.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'products/books.html', context)

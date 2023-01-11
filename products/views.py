from django.shortcuts import render, get_object_or_404
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


def book_detail(request, book_id):
    """
    A view to show all book products available for sale.
    """
    book = get_object_or_404(Books, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'products/book-detail.html', context)

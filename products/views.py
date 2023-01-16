from django.shortcuts import render, get_object_or_404
from .models import Books, Genre


def books(request):
    """
    A view to show all book products available for sale.
    """
    books = Books.objects.all()
    genres = None
    all_genres = Genre.objects.all()

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            books = books.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    context = {
        'books': books,
        'genres': genres,
        'all_genres': all_genres,
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

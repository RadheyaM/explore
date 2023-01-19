from django.shortcuts import render, get_object_or_404
from .models import Books, Genre, Posters


def books(request):
    """
    A view to show all book products available for sale.
    """
    books = Books.objects.all()
    genres = None
    all_genres = Genre.objects.filter(pk__lte=5)

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            books = books.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    template = 'products/books.html'
    context = {
        'books': books,
        'genres': genres,
        'all_genres': all_genres,
    }

    return render(request, template, context)

def posters(request):
    """
    A view to show all poster products available for sale.
    """
    posters = Posters.objects.all()
    genres = None
    all_genres = Genre.objects.filter(pk__gte=6)

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            posters = posters.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    template = 'products/posters.html'
    context = {
        'posters': posters,
        'genres': genres,
        'all_genres': all_genres,
    }

    return render(request, template, context)


def book_detail(request, book_id):
    """
    A view to show all book products available for sale.
    """
    book = get_object_or_404(Books, pk=book_id)
    genre = book.genre
    genres = Books.objects.filter(genre=genre)
    recommend = genres.exclude(pk=book_id)

    template = 'products/book-detail.html'
    context = {
        'book': book,
        'recommend': recommend,
    }

    return render(request, template, context)


def poster_detail(request, poster_id):
    """
    A view to show all book products available for sale.
    """
    poster = get_object_or_404(Posters, pk=poster_id)
    genre = poster.genre
    genres = Posters.objects.filter(genre=genre)
    recommend = genres.exclude(pk=poster_id)

    template = 'products/poster-detail.html'
    context = {
        'poster': poster,
        'recommend': recommend,
    }

    return render(request, template, context)

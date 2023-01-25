from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q


from .models import Books, Genre, Posters

def books(request):
    """
    A view to show all book products available for sale.
    """
    books = Books.objects.all()
    search = None
    result_count = None
    genres = None
    all_genres = Genre.objects.filter(pk__lte=5)

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            books = books.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, 'You need to enter a search term in the search bar to search books.')
                return redirect(reverse('books'))
            
            # might be overkill but would like to avoid the user getting no results.
            search_terms = Q(
                title__icontains=search
                ) | Q(
                    author__icontains=search
                    ) | Q(
                        genre__name__icontains=search
                        ) | Q(
                            subtitle__icontains=search
                            ) | Q(
                                description__icontains=search
                                )

            books = books.filter(search_terms)
            result_count = books.count()
            
            if result_count == 0:
                result_count == None
                messages.info(request, f'No books found with search term "{search}"')
                return redirect(reverse('books'))

    template = 'products/books.html'
    context = {
        'books': books,
        'genres': genres,
        'all_genres': all_genres,
        'search': search,
        'result_count': result_count
    }

    return render(request, template, context)

def posters(request):
    """
    A view to show all poster products available for sale.
    """
    posters = Posters.objects.all()
    search = None
    genres = None
    all_genres = Genre.objects.filter(pk__gte=6)

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            posters = posters.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, 'You need to enter a search term in the search bar to search posters.')
                return redirect(reverse('posters'))
            
            search_terms = Q(
                name__icontains=search
                ) | Q(
                    genre__name__icontains=search
                    ) | Q(description__icontains=search)

            posters = posters.filter(search_terms)

            if posters.count() == 0:
                messages.info(request, f'No posters found with search term "{search}"')
                return redirect(reverse('posters'))


    template = 'products/posters.html'
    context = {
        'posters': posters,
        'genres': genres,
        'all_genres': all_genres,
        'search': search,
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

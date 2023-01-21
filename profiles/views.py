from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from products.models import Books, Posters


def profile(request):
    """
    A view to show the user profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully updated your profile!')

    template = 'profile/profile.html'
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)

def wishlist(request):
    """
    display the wishlist page
    """
    posters = Posters.objects.filter(user_poster_wishlist=request.user)
    books = Books.objects.filter(user_book_wishlist=request.user)
    template = 'profile/wishlist.html'
    context = {
        'posters': posters,
        'books': books,
    }

    return render(request, template, context)

def edit_book_wishlist(request, id):
    """
    Add or remove item from wishlist
    """
    product = get_object_or_404(Books, pk=id)
    if product.user_book_wishlist.filter(id=request.user.id):
        product.user_book_wishlist.remove(request.user)
        messages.success(request, f'Removed from Wishlist.')
    else:
        product.user_book_wishlist.add(request.user)
        messages.success(request, f'Added to Wishlist.')
        
    return redirect(reverse('wishlist'))
    

def edit_poster_wishlist(request, id):
    """
    Add or remove item from wishlist
    """
    product = get_object_or_404(Posters, pk=id)
    if product.user_poster_wishlist.filter(id=request.user.id):
        product.user_poster_wishlist.remove(request.user)
        messages.success(request, f'Removed from Wishlist.')
    else:
        product.user_poster_wishlist.add(request.user)
        messages.success(request, f'Added to Wishlist.')
        
    return redirect(reverse('wishlist'))
    
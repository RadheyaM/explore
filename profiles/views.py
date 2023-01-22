from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy

from checkout.models import Order
from .models import UserProfile, Contact, SiteReview
from .forms import UserProfileForm

from products.models import Books, Posters

def delivery_address(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully updated your profile!')

    template = 'profile/delivery-details.html'
    form = UserProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, template, context)

def order_history(request):
    
    template = 'profile/order-history.html'
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    context = {
        'orders': orders,
    }

    return render(request, template, context)

def order_history_detail(request, order_number):
    
    template = 'checkout/checkout-success.html'
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
        'from_profile': True,
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


class ContactUs(CreateView):
    """
    View for a User to Create a contact message
    """
    model = Contact
    fields = ('email', 'reason', 'body',)
    template_name = 'profile/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "Thank you for your message! We will respond as soon as possible"
        )

        return super().form_valid(form)

class CreateSiteReview(CreateView):
    """
    View for a User to Create a site reivew
    """
    model = SiteReview
    fields = ('name', 'title', 'rating', 'body',)
    template_name = 'profile/site-review.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, 
            messages.SUCCESS, 
            "Thank you for your review! Once approved it will be displayed on the site!"
        )

        return super().form_valid(form)
    
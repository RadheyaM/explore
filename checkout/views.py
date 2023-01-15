"""based on project boutique ado code"""
from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    """
    Render a view for the checkout
    """
    basket = request.session.get('basket', {})
    # if not basket:
    #     message.error(request, "There's nothing in your bag, better keep on shopping there buddy.")
    #     return redirect(reverse('books'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MOja9GRqR0b7FUtJwlJHqFhnN5WhXXcSMx7cyUwZWyMzgNqanRT858TaJagYRjuM9TfdMZcs9xego30AgediDjP00xomNU3pn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
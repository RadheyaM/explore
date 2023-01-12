"""based on project boutique ado code"""
from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    """
    Render a view for the checkout
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your bag, better keep on shopping there buddy.")
        return redirect(reverse('books'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form: order_form,'
    }

    return render(request, template, context)
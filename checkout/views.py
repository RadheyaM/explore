from django.shortcuts import render


def checkout(request):
    """
    Render a view for the checkout
    """
    return render(request, 'checkout/checkout.html')
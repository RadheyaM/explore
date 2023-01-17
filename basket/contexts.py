"""
Code based on that of project walkthrough boutique ado
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Books
from profiles.models import UserProfile, User

def basket_contents(request):

    basket_items =[]
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    total_ten_percent = 0
    first_order = False

    try:
        profile = get_object_or_404(UserProfile, user=request.user)
        first_order = profile.first_order
    except:
        first_order = False

    for item_id, quantity in basket.items():
        product = get_object_or_404(Books, pk=item_id)
        total += quantity * product.price
        subtotal = quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    ten_percent = (total / 100) * 10
    if first_order == True:
        total_ten_percent = Decimal(total - ten_percent)
        grand_total = total_ten_percent + delivery
    else:
        grand_total = total + delivery

    context ={
        'basket_items': basket_items,
        'total': total,
        'total_ten_percent': total_ten_percent,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'first_order': first_order,
        'ten_percent': ten_percent,
    }

    return context
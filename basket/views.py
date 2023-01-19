"""Code based upon that of the walkthrough project boutique ado"""

from django.shortcuts import render, redirect


def basket(request):
    """
    A view to display the user basket.
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a qty of a particular item to the shopping basket
    """

    quantity =  int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    material_size = None
    if 'product_material_size' in request.POST:
        material_size = request.POST['product_material_size']
    basket = request.session.get('basket', {})

    if material_size:
        if item_id in list(basket.keys()):
            if material_size in basket[item_id]['items_by_material_size'].keys():
                basket[item_id]['items_by_material_size'][material_size] += quantity
            else:
                basket[item_id]['items_by_material_size'][material_size] = quantity
        else:
            basket[item_id] = {'items_by_material_size': {material_size: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)

"""Code based upon that of the walkthrough project boutique ado"""
from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Books, Posters

def basket(request):
    """
    A view to display the user basket.
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a qty of a particular item to the shopping basket
    """
    try:
        product = Books.objects.get(code=item_id)
    except:
        product = Posters.objects.get(code=item_id)

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
                messages.success(request, f'Success! You added {product} to your basket!')
            else:
                basket[item_id]['items_by_material_size'][material_size] = quantity
                messages.error(request, f'Success! You added {product} to your basket!')
        else:
            basket[item_id] = {'items_by_material_size': {material_size: quantity}}
            messages.warning(request, f'Success! You added {product} to your basket!')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.info(request, f'Success! You added {product} to your basket!')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Success! You added {product} to your basket!')
    
    

    request.session['basket'] = basket
    return redirect(redirect_url)

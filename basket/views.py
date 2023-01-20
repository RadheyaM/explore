"""Code based upon that of the walkthrough project boutique ado"""
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
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
                messages.success(request, f'Success! You updated {product} ({material_size}) qty in your basket!')
            else:
                basket[item_id]['items_by_material_size'][material_size] = quantity
                messages.success(request, f'Success! You added {material_size} Poster: {product} to your basket!')
        else:
            basket[item_id] = {'items_by_material_size': {material_size: quantity}}
            messages.success(request, f'Success! You added {material_size} Poster: {product} to your basket!')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Success! You updated {product} qty in your basket.')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Success! You added {product} to your basket.')
    
    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id, material_size):
    """
    remove an item from the basket
    """
    try:
        material_size = material_size
        if material_size == 'nothing':
            material_size = None
        basket = request.session.get('basket', {})

        if material_size:
            print(material_size)
            del basket[item_id]['items_by_material_size'][material_size]
            if not basket[item_id]['items_by_material_size']:
                basket.pop(item_id)
        else:
            print('no material size found')
            basket.pop(item_id)
        request.session['basket'] = basket
        messages.success(request, 'You removed the item from your basket!')
        return redirect(reverse('basket'))
    except Exception as e:
        return HttpResponse(status=500)

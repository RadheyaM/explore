from django.shortcuts import render


def basket(request):
    """
    A view to display the user basket.
    """
    return render(request, 'basket/basket.html')


from django import template

register = template.library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
from decimal import Decimal
from django import template
from coupons.models import Coupon

register = template.Library()



@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


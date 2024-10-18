from decimal import Decimal
from django import template
from coupons.models import Coupon

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@property

def coupon(self):
    if self.coupon_id:
        try:
            return Coupon.objects.get(id=self.coupon_id)
        except Coupon.DoesNotExist:
            pass
        return None

def get_discount(self):
    if self.coupon:
        return (self.coupon.discount / Decimal(100)) \
            * self.get_total_price()

def get_total_price_after_discount(self):
    return self.get_total_price() - self.get_discount()
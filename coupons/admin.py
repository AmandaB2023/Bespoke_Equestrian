from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount',
                    'valid_from', 'valid_to', 'active', 'is_used']
    list_filter = ['active', 'valid_from', 'valid_to', 'discount']
    search_fields = ['code']

admin.site.register(Coupon, CouponAdmin)

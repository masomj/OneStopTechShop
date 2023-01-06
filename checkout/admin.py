from django.contrib import admin
from .models import order, orderItem
# Register your models here.

class itemAdmin(admin.ModelAdmin):
    readonly_fields=('orderitem_total',)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'payment_due')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town','city', 'street_name', 'delivery_cost',
              'order_total', 'payment_due')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'payment_due',)

    ordering = ('-date',)

admin.site.register(order, OrderAdmin)
admin.site.register(orderItem, itemAdmin)
    

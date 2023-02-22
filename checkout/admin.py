from django.contrib import admin
from .models import order, orderItem
# Register your models here.

class ItemAdminInline(admin.TabularInline):
    model = orderItem
    
class OrderAdmin(admin.ModelAdmin):
    
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'payment_due')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town','city', 'street_name','house_number', 'delivery_cost',
              'order_total', 'payment_due','payed')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'payment_due',)

    ordering = ('-date',)

admin.site.register(order, OrderAdmin)
admin.site.register(orderItem)

    

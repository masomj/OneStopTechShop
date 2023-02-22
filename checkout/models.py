from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User

import uuid

# Create your models here.

class order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    order_number=models.UUIDField(default=uuid.uuid4,editable=False, max_length=100)
    full_name=models.CharField(max_length=50, null=False, blank=False)
    email=models.CharField(max_length=64, null=False)
    phone_number=models.CharField(max_length=11, null=False)
    country=models.CharField(max_length=64, null=False)
    postcode=models.CharField(max_length=7, null=False)
    town=models.CharField(max_length=64, null=False)
    city=models.CharField(max_length=64, null=False)
    street_name=models.CharField(max_length=100, null=False)
    house_number=models.CharField(max_length=5,null=False)
    date=models.DateField(auto_now_add=True)
    delivery_cost=models.DecimalField(max_digits=6, decimal_places=2 ,null=True, default=0)
    order_total=models.DecimalField(max_digits=11, decimal_places=2 ,null=False, default=0)
    payment_due=models.DecimalField(max_digits=11, decimal_places=2 ,null=False, default=0)
    payed=models.BooleanField(default=False)
    
   
    
    def update_total(self):
        self.order_total = self.orderItem.aggregate(Sum('orderitem_total'))['orderitem_total__sum']
        self.payment_due= self.delivery_cost + self.order_total
        self.save()


class orderItem(models.Model):
    order = models.ForeignKey(order, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    product = models.ForeignKey('products.Product', null=False, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
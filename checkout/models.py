from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product

# Create your models here.

class order(models.Model):
    order_number=models.CharField(max_length=64, null=False, editable=False)
    full_name=models.CharField(max_length=50, null=False, blank=False)
    email=models.CharField(max_length=64, null=False)
    phone_number=models.IntegerField(null=False)
    country=models.CharField(max_length=64, null=False)
    postcode=models.CharField(max_length=7, null=False)
    town=models.CharField(max_length=64, null=False)
    city=models.CharField(max_length=64, null=False)
    street_name=models.CharField(max_length=100, null=False)
    house_number=models.IntegerField(null=False)
    date=models.DateField(auto_now_add=True)
    delivery_cost=models.DecimalField(max_digits=6, decimal_places=2 ,null=True, default=0)
    order_total=models.DecimalField(max_digits=11, decimal_places=2 ,null=False, default=0)
    payment_due=models.DecimalField(max_digits=11, decimal_places=2 ,null=False, default=0)

class orderItem(models.Model):
    order = models.ForeignKey(order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderItem')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
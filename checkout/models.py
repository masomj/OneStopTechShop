from django.db import models

# Create your models here.

class order (models.Model):
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

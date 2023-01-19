from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class review(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING) #allow deleted user account reviews to persist
    rating = models.IntegerField(null=False)
    review = models.TextField(max_length=5000, null=False)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    

from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

# Create your models here.

class review(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING) #allow deleted user account reviews to persist
    rating = models.IntegerField(null=False)
    review = models.TextField(max_length=5000, null=False)
    product = models.ForeignKey('products.Product', null=False, on_delete=models.CASCADE)
    
    
    
    

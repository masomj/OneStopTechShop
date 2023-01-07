from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userDetails(models.Model):
    user_id = models.ForeignKey(User,null=False,  on_delete=models.CASCADE)
    full_name = models.CharField(max_length=256, default="", blank=True)
    email = models.CharField(max_length=256, blank=True)
    postcode = models.CharField(max_length=7, default="", blank=True)
    house_number=models.IntegerField()
    phone_number=models.IntegerField()
    street_name=models.CharField(max_length=256,default="", blank=True)
    city=models.CharField(max_length=256, default="", blank=True)
    country=models.CharField(max_length=256,default="",blank=True)
    town=models.CharField(max_length=256, default="",blank=True)
    

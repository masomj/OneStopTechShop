from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userDetails(models.Model):
    user_id = models.ForeignKey(User,null=False,  on_delete=models.CASCADE)
    postcode = models.CharField(max_length=7)
    house_number=models.IntegerField()
    street_name=models.CharField(max_length=256)
    city=models.CharField(max_length=256)

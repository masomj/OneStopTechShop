from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.models import User

# Create your models here.

class userDetails(models.Model):
    user_id = models.ForeignKey(User,null=False,  on_delete=models.CASCADE)
    postcode = models.CharField(max_length=7)
    house_number=models.IntegerField()
    street_name=models.CharField(max_length=256)
    city=models.CharField(max_length=256)


=======

# Create your models here.
>>>>>>> 893dcc3af98d6eb58b6e6b93375273009b5f269c
=======

# Create your models here.
>>>>>>> 893dcc3af98d6eb58b6e6b93375273009b5f269c

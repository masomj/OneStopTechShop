from email.policy import default
from unicodedata import category
from django.db import models
from django.db.models import Sum
from reviews.models import review




# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Sub_Categories'
    name = models.CharField(max_length=254) 
    parentCategory = models.ForeignKey('CategoryParent',null=True,blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class CategoryParent(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=254,null=False, blank=True)
    brand =models.CharField(max_length=254,null=False, blank=True)
    sku = models.CharField(max_length=254, null=False, blank=True)
    price=models.DecimalField(max_digits=12, decimal_places = 2, null=False, blank=True)
    currency=models.CharField(max_length=254,null=False, blank=True)
    image_url=models.URLField(null=False,blank=True)
    category=models.ForeignKey('Category',null=False, blank=True, on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=10000, null=False, blank=True)
    average_rating=models.CharField(max_length=254,null=False, blank=True)
    reviews_count= models.IntegerField(null=False, blank=True)
    has_sizes = models.BooleanField(default=False, null=False, blank=True)

    def __str__(self):
        return self.title
    
    def update_average_rating(self):
        product_reviews_count = review.objects.filter(product=self).count()
        rating_sum = review.objects.filter(product=self).aggregate(Sum('rating'))['rating__sum']
        print(rating_sum)
        self.average_rating = rating_sum / product_reviews_count
        self.reviews_count = product_reviews_count
        self.save()
        
    
from django.shortcuts import render
from products.models import Product, Category, CategoryParent

# Create your views here.

def index(request):
    categories = Category.objects.all()
    parent_categories = CategoryParent.objects.all()
    context={
        'categories':categories,
        'parent_categories':parent_categories
    }
    for category in categories:
        print(category.parentCategory)
     
    
    return render(request,'index.html',context)
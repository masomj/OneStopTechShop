from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import Product, Category

# Create your views here.

def products(request):
    products = Product.objects.all()
    context={
        'products':products
    }
    return render(request,'products.html',context)

def productInfo(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    
    context={
        'product':product
    }
    print(product.category.name)
    
    return render(request,'productInfo.html',context)
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import review
# Create your views here.

@login_required
def leave_a_review(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    if request.method == "POST":
        
        
        review_obj = review.objects.create(
            user_id = request.user,
            rating = request.POST['rating'],
            review = request.POST['rating_val'],
            product = product,
        )
        review_obj.save()
        
    
    context = {
        'product':product
    }
    return render(request, 'reviews.html', context)
    
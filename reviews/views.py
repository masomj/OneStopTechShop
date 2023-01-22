from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from checkout.models import order, orderItem
from .models import review
# Create your views here.

@login_required
def leave_a_review(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    
    users_orders = order.objects.filter(user = request.user) 
    
    product_orders = users_orders.filter(orderItem__product=product)
    if product_orders.count() > 0:
        if request.method == 'POST':
            print('post')
            review_obj = review.objects.create(
                user_id = request.user,
                rating = request.POST['rating'],
                review = request.POST['review'],
                product = product,
            )
            review_obj.save()
            
            return  redirect(reverse('products'))
        
        context = {
            'product':product
        }
        return render(request, 'reviews.html', context)
    else:
        messages.warning(request, 'You have not purchased this item, therefore you cannot leave a review.')
        return redirect(reverse('products'))
            
    
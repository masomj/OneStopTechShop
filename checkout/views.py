from django.shortcuts import render, get_object_or_404, redirect, reverse
from userprofile.models import userDetails
from django.contrib.auth.models import User
from django.conf import settings
from bag.contexts import bag_contents
from .models import order, orderItem
from products.models import Product
import stripe



# Create your views here
def checkout(request):    
    
    
    if request.user.is_authenticated:
        logged_in_user = request.user.id
        userObj = get_object_or_404(User, pk=logged_in_user)
        userdetails = get_object_or_404(userDetails, user_id=userObj.id)
        context ={
        'userdetails':userdetails
        }
    else:
        context ={
        }
    if request.method == 'POST':
        bag = request.session.get('bag',{})
        order_details = order.objects.create(
            postcode = request.POST['postcode'],
            house_number = request.POST['house_number'],
            street_name=request.POST['street_name'],
            city=request.POST['city'],
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            phone_number = request.POST['phone_no'],
            country=request.POST['country'],
            town = request.POST['town'],
          )
        order_details.save()
        
        for item_id, item_data in bag.items():
            print(item_id)
            print(item_data)
            product=Product.objects.get(id=item_id)
            orderitem = orderItem.objects.create(
                order = order_details,
                product= product,
                quantity=item_data,
           )
            orderitem.save()
            request.session['order_id'] = order_details.id
        return redirect(reverse('pay'))
   

    return render(request,'checkout.html', context)


def pay(request):
   
    
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100) # convert £ value to pence
    public = settings.STRIPE_PUBLISHABLE_KEY
    private = settings.STRIPE_SECRET_KEY
    pending_order = get_object_or_404(order, id=request.session['order_id'])
    stripe.api_key = private
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency = settings.STRIPE_CURRENCY,)
    
    context={
        'stripe_public_key':public,
        'client_secret':intent.client_secret
    }
    
    ## if successful statement
    if request.method =='POST':
        bag = request.session.get('bag',{})
        bag.clear()
        request.session['bag'] = bag
        return redirect(reverse('products'))
    
    return render(request,'stripe_checkout.html', context)
    
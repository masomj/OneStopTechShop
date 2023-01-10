from django.shortcuts import render, get_object_or_404
from userprofile.models import userDetails
from django.contrib.auth.models import User
from django.conf import settings
from bag.contexts import bag_contents
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
    
   

    return render(request,'checkout.html', context)


def pay(request):
    
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100) # convert £ value to pence
    public = settings.STRIPE_PUBLISHABLE_KEY
    private = settings.STRIPE_SECRET_KEY
    
    stripe.api_key = private
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency = settings.STRIPE_CURRENCY,
    
        
    )
    print(intent)
    context={
        'stripe_public_key':public,
        'client_secret':intent.client_secret
    }
    return render(request,'stripe_checkout.html', context)
    
from django.shortcuts import render, get_object_or_404, redirect, reverse
from userprofile.models import userDetails
from django.contrib.auth.models import User
from django.conf import settings
from bag.contexts import bag_contents
from .models import order, orderItem
from products.models import Product
import stripe
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
def completedCheckout(request, order_id): 
    current_order = get_object_or_404(order, pk=order_id)  
    ordered_items = orderItem.objects.filter(order = current_order)
    context = {
        'order':current_order,
        'ordered_items':ordered_items
    }
    
    return render(request, 'successfulOrder.html',context)
    

# Create your views here
def checkout(request):    
    
    if request.user.is_authenticated:
        logged_in_user = request.user.id
        userObj = get_object_or_404(User, pk=logged_in_user)
        userdetails = userDetails.objects.filter(user_id=userObj)
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
        if request.user.is_authenticated:
            order_details.user = request.user
        order_details.save()
        
        for item_id, item_data in bag.items():
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
        subject, from_email, to = 'Order Summary', 'onestoptechclinic@gmail.com',f'{pending_order.email}'
        html_content = f'<h3> Thanks for your order </h3><div><p>The total cost is £ {pending_order.payment_due}</p></div><div><p>The order reference number is {pending_order.order_number}</p></div><div>If You believe there has been an error, please reach out to our support team by replying to this email.</div><div><h4>One Stop Tech Shop</h4></div>'
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        
        bag = request.session.get('bag',{})
        bag.clear()
        request.session['bag'] = bag
        pending_order.payed = True
        pending_order.save()
        return redirect(reverse('completedCheckout', args=[pending_order.id] ))
    
    return render(request,'stripe_checkout.html', context)
    
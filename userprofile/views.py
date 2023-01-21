from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import userDetails
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from checkout.models import order
from django.contrib import messages


# Create your views here.
@login_required
def profile(request):
    logged_in_user = request.user.id
    userObj = get_object_or_404(User, pk=logged_in_user)
    userdetails = get_object_or_404(userDetails, user_id=userObj.id)
    if userdetails.email == "":
        email = userObj.email
    else:
        email = userdetails.email
    
    context={
        'userdetails':userdetails,
        'email':email
    }
    print(userdetails.postcode)
    
    if request.method=='POST':
        userdetails.user_id = request.user
        userdetails.postcode = request.POST['postcode']
        userdetails.house_number = request.POST['house_number']
        userdetails.street_name=request.POST['street_name']
        userdetails.city=request.POST['city']
        userdetails.full_name = request.POST['full_name']
        userdetails.email = request.POST['email']
        userdetails.phone_number = request.POST['phone_no']
        userdetails.country=request.POST['country']
        userdetails.town = request.POST['town']
        userdetails.save()
        return redirect(reverse('products'))
    
    return render(request, 'profile.html',context)

@login_required
def view_orders(request):
    users_orders = order.objects.filter(user = request.user)
    if users_orders.count() < 1 :
        messages.warning(request, 'You have no previous orders.')
        return redirect(reverse('profile'))
    
    context = {
        'user_orders':users_orders
        
    }
    
    return render(request,'orders.html', context)



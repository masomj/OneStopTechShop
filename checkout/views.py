from django.shortcuts import render, get_object_or_404
from userprofile.models import userDetails
from django.contrib.auth.models import User



# Create your views here.

def checkout(request):
    bag = request.session.get('bag',{})
    
    logged_in_user = request.user.id
    
    userObj = get_object_or_404(User, pk=logged_in_user)
    userdetails = get_object_or_404(userDetails, user_id=userObj.id)
    
    context ={
        'userdetails':userdetails
    }

    return render(request,'checkout.html', context)
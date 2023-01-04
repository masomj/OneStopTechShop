from django.shortcuts import render, get_object_or_404
from .models import userDetails
from django.contrib.auth.models import User


# Create your views here.

def profile(request):
    logged_in_user = request.user.id
    userdetails = get_object_or_404(userDetails, pk=logged_in_user)
    print(logged_in_user)
    
    context={
        'user':logged_in_user,
        'userdetails':userdetails,
    }
    print(userdetails.postcode)
    
    if request.method=='POST':
        userdetails.user_id = request.user
        userdetails.postcode = request.POST['postcode']
        userdetails.house_number = request.POST['number']
        userdetails.street_name=request.POST['street']
        userdetails.city=request.POST['city']
    return render(request, 'profile.html',context)




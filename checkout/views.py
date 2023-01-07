from django.shortcuts import render, get_object_or_404
from userprofile.models import userDetails



# Create your views here.

def checkout(request):
    bag = request.session.get('bag',{})
    logged_in_user = request.user.id
    print(logged_in_user)
    print(get_object_or_404(userDetails, pk=logged_in_user))
    userdetails = get_object_or_404(userDetails, pk=logged_in_user)
    context ={
        'user_details':userdetails
    }

    return render(request,'checkout.html', context)
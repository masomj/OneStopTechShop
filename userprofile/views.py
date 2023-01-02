<<<<<<< HEAD
<<<<<<< HEAD
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
    return render(request, 'profile.html',context)
=======
=======
>>>>>>> 893dcc3af98d6eb58b6e6b93375273009b5f269c
from django.shortcuts import render

# Create your views here.


def profile(request):
<<<<<<< HEAD
    return render(request, 'profile.html')
>>>>>>> 893dcc3af98d6eb58b6e6b93375273009b5f269c
=======
    return render(request, 'profile.html')
>>>>>>> 893dcc3af98d6eb58b6e6b93375273009b5f269c

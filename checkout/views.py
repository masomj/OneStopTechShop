from django.shortcuts import render
from .forms import orderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag',{})
    order_form = orderForm()
    
    context={
        'order_form':order_form
    }
    return render(request,'checkout.html',context)
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.contrib import messages

def bag(request):
    bag = request.session.get('bag',{})
    is_empty = bool(bag)
    if is_empty == False:
        messages.warning(request, 'You have no items in your bag. Please add a product to continue.')
        return redirect(reverse('products'))
    elif is_empty == True:
        return render(request,'view_bag.html')

def add_to_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url=request.POST.get('redirect_url')
    size = None
    if 'product_size'in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag',{})
    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['items_by_size'].keys():
                    bag[product_id]['items_by_size'][size]+= quantity
            else:
                 bag[product_id]['items_by_size'][size]=quantity
        else:
            bag[product_id]= {'items_by_size': {size:quantity}}
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
        else:
            bag[product_id] = quantity
        
    request.session['bag'] = bag
    messages.success(request, 'Added To Bag')
    return redirect(redirect_url)

def update_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag',{})

    if product_id in list(bag.keys()):
        bag[product_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_item(request, product_id):
    bag = request.session.get('bag',{})
    bag.pop(product_id)
    request.session['bag'] = bag

    return redirect(reverse('bag'))





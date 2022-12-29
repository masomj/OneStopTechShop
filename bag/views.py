from django.shortcuts import render,redirect,reverse,HttpResponse

def bag(request):

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
    return redirect(redirect_url)

def update_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag',{})

    if product_id in list(bag.keys()):
        bag[product_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)





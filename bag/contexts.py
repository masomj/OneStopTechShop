from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items =[]
    total=0
    product_count=0
    bag=request.session.get('bag',{})

    for item_id,item_data in bag.items():
        if isinstance(item_data,int):
            product = get_object_or_404(Product, pk=item_id)
            total+=  item_data * product.price
            bag_items.append({
                'item_id':item_id,
                'quantity':item_data,
                'product':product
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                product = get_object_or_404(Product, pk=item_id)
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id':item_id,
                    'quantity':quantity,
                    'product':product,
                    'size':size,})
    delivery = 0                    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,      
    }
    return context


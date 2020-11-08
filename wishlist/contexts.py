from decimal import Decimal 
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):

    products = []
    wishlist_items = []
    wishlist = request.session.get('wishlist', [])

    for item_id in wishlist:
        product = get_object_or_404(Product, pk=item_id)
 
        products.append({
            'item_id': item_id,
            'product': product,
        }
        )

    for item_id in wishlist:
        
             wishlist_items.append(
                item_id
             )

    context = {
        'wishlist_items': wishlist,
        'products': products,
    }


    return context



from decimal import Decimal 
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):

    wishlist_items = []
    wishlist = request.session.get('wishlist', [])
 

    for item_id in wishlist:
        
             wishlist_items.append(
                item_id
             )

    context = {
        'wishlist_items': wishlist,
    }


    return context



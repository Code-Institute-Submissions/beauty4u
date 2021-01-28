from decimal import Decimal 
from django.conf import settings
from django.shortcuts import get_object_or_404, HttpResponse
from products.models import Product
from management.models import Sitesettings
import datetime
from management.models import Sitesettings


def cart_contents(request):


    free_shipping_setting = get_object_or_404(Sitesettings, name="Free Shipping Threshold")
    shipping_cost = get_object_or_404(Sitesettings, name="Standard Shipping")
    std_shipping = shipping_cost.value
    threshold = free_shipping_setting.value


    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
 

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        if product.sale_price is not None:
            if product.sale_price < product.price:
               total += quantity * product.sale_price
        else:
            total += quantity * product.price
        product_count += quantity

        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        }
        )


    if total < threshold:
        shipping = std_shipping
        free_shipping_delta =  threshold - total

    else: 
        shipping = 0
        free_shipping_delta = 0


    grand_total = shipping + total


    #date for copyright included in context to display on all pages
    now = datetime.datetime.now()
    currentyear = now.year

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold':  threshold,
        'grand_total': grand_total,
        'current_year': currentyear,

    }


    return context


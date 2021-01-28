from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product 
from django.contrib import messages
from django.views.decorators.http import require_POST
from decimal import Decimal 
from django.conf import settings
from django.shortcuts import get_object_or_404, HttpResponse
from management.models import Sitesettings
import datetime
from cart.contexts import cart_contents
import stripe
from django.http import JsonResponse


@require_POST
def add_to_cart(request):

    """ 
    A view to handle POST requests to add items to the cart 
    Takes posted data from cart.js

    """

    item_id = request.POST.get('product_id')
    quantity = int(request.POST.get('product_quantity'))

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity

    else:
        cart[item_id] = quantity
       
    request.session['cart'] = cart
    request.session.modified = True

    return HttpResponse(status=200)    


def refresh_cart(request):

    
    """ 
    A view to handle GET request to return updated cart html and return it to the frontend 
    Takes GET request from cart.js
    
    """

    free_shipping_setting = get_object_or_404(Sitesettings, name="Free Shipping Threshold")
    shipping_cost = get_object_or_404(Sitesettings, name="Standard Shipping")
    std_shipping = shipping_cost.value
    threshold = free_shipping_setting.value

    total = 0
    product_count = 0
    cart_items = []
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
        request.session.modified = True


    if total < threshold:
        shipping = std_shipping
        free_shipping_delta =  threshold - total

    else: 
        shipping = 0
        free_shipping_delta = 0


    grand_total = shipping + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold':  threshold,
        'grand_total': grand_total,

    }

    return render(request, 'cart/cart.html', context)




def adjust_cart(request):

    """ 
    A view used to delete products from the cart
    Takes posted information from cart.js

    """
    
    cart = request.session.get('cart', {})
    product_id = request.POST.get('product_id')

    del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return HttpResponse(status=200)

@require_POST
def change_shipping_method(request):

    """
    A view to take posted information from shipping.js and update Stripe payment intent with new shipping selection cost
    Reutns new total, shipping method, and cost to the frontend 
    
    """
    shipping_method = ""
    current_cart = cart_contents(request)
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    intent_id = request.POST.get('intent_id')
    selected_method = request.POST.get('selected')

    #Get standard shipping costs from database
    free_shipping_setting = get_object_or_404(Sitesettings, name="Free Shipping Threshold")
    shipping = get_object_or_404(Sitesettings, name="Standard Shipping")
    std_shipping = shipping.value
    threshold = free_shipping_setting.value
    shipping_cost = shipping.value

    #Use Selected variable posted 
    if selected_method == "1":
        shipping_method = "standard"
        stripe_ship = "Standard Delivery"
        if current_cart['total'] < threshold:
            shipping_cost = std_shipping
        else:
            shipping_cost = 0
    elif selected_method == "2":
        shipping_method = "collect"
        stripe_ship = "Click & Collect"
        shipping_cost = 0
    else: 
        shipping_method = "standard"
        stripe_ship = "Standard Delivery"
        shipping_cost = std_shipping

    #Calculate the total based on shipping method selected and shipping cost 
    total = Decimal(shipping_cost) + current_cart['total']   

    #Check to see if any discount is applied
    if 'discount_total' in request.session:
        total = Decimal(shipping_cost) + Decimal(request.session['discount_subtotal'])
        total = round(total, 2)


    # Modify Stripe payment intent to reflect new total based on shipping selection
    stripe_total = round(total * 100) 
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.modify(
        intent_id,
        amount=stripe_total, 
        currency=settings.STRIPE_CURRENCY,
        description=stripe_ship,
        )


    request.session['shipping_cost'] = int(shipping_cost)
    # Update session variable with shipping method selected
    request.session['shipping_method'] = stripe_ship
    data = {
        'total': total,
        'shipping_method': shipping_method,
        'shipping_cost': shipping_cost,
    }


    return JsonResponse(data)

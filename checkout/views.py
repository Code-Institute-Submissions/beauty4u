from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
import stripe
import json
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .models import OrderLineItem, Order
from cart.contexts import cart_contents
from management.models import Sitesettings, Coupons
from django.http import JsonResponse
from decimal import Decimal


@require_POST
def cache_checkout_data(request):

    """
    A view to cache checkout data in the stripe payment intent

    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Create your views here.
def checkout(request):

    """
    A view that returns the checkout template and creates the
    initial Stripe payment intent

    """

    # Assume click and collect is not available until check is complete
    click_and_collect = False
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.shipping_method = request.session['shipping_method']
            order.original_cart = json.dumps(cart)
            current_cart = cart_contents(request)
            subtotal = current_cart['total']
            free_ship_thres = Sitesettings.objects.get(
                                        name="Free Shipping Threshold")
            threshold_value = free_ship_thres.value
            std_shipping_cost = Sitesettings.objects.get(
                                        name="Standard Shipping")
            std_value = std_shipping_cost.value
            if request.session['shipping_method'] == "Standard":
                if subtotal > threshold_value:
                    order.delivery_cost = 0
                    order.subtotal = subtotal
                    order.total = subtotal
                else:
                    order.total = subtotal + std_value
                    order.subtotal = subtotal
                    order.delivery_cost = std_value
            elif order.shipping_method == "Click & Collect":
                order.subtotal = subtotal
                order.total = subtotal

            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(order=order,
                                                    product=product,
                                                    quantity=item_data)
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request,
                                   ("Product not in database."
                                    "Please contact us!")
                                   )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was a problem with your order form.'
                                    'Please double check your details')
            return redirect(reverse('checkout'))

    else:

        # Redirect user back to the shop if their cart is empty
        cart = request.session.get('cart', {})
        if not cart:
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']

        std_shipping_cost = Sitesettings.objects.get(name="Standard Shipping")
        std_value = std_shipping_cost.value
        free_ship_thres = Sitesettings.objects.get(
                                               name="Free Shipping Threshold")
        threshold_value = free_ship_thres.value

        # When the checkout view is loaded - reset any discounts
        # that may be stored
        if 'discount_total' in request.session:
            del request.session['discount_total']
            del request.session['discount_subtotal']

        # Default shipping method and cost to standard anytime
        # the checkout view is accessed
        request.session['shipping_method'] = 'Standard'
        if current_cart['total'] < threshold_value:
            request.session['shipping_cost'] = str(std_value)
        else:
            request.session['shipping_cost'] = 0
        # Check to see if click and collect is enabled
        collect = get_object_or_404(Sitesettings, name="Click & Collect")

        # If they have click and collect enabled
        if collect.status:
            click_and_collect = True

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            description="Standard Delivery",
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()

        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'click_and_collect': click_and_collect,
        'intent_id': intent.id,
        'current_cart': current_cart

        }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):

    """
    A view that is returned on successful checkout

    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully placed! \
        Your order number is {order_number}. A confirmation email \
            will be send to {order.email} ')

    if 'cart' in request.session:
        del request.session['cart']

    if 'shipping_method' in request.session:
        del request.session['shipping_method']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)


@require_POST
def apply_coupon(request):

    """
    A view to handling applying coupons
    Checks if minimum spend is required
    Checks if coupon is active
    Takes posted information from coupon.js

    """
    result = ""
    coupon_code = request.POST.get('coupon_code')
    intent_id = request.POST.get('intent_id')

    # Get the subtotal of the order
    current_cart = cart_contents(request)
    subtotal = Decimal(current_cart['total'])

    try:
        coupon = Coupons.objects.get(code__iexact=coupon_code)
    except Coupons.DoesNotExist:
        result = "Sorry! We couldn't find a coupon that matches your code!"
        return HttpResponse(result)

    if not coupon.active:
        result = "Sorry! That coupon is not available! It may have expired."
        return HttpResponse(result)
    if coupon.minspend > subtotal:
        result = f"Whoops! This coupon requires you to \
                   spend a minimum of €{coupon.minspend}"
        return HttpResponse(result)

    coupon_savings = coupon.discount
    percentage = coupon.discount
    percentage = percentage / 100
    discount = Decimal(percentage) * Decimal(subtotal)

    stripe_total = round(subtotal - discount, 2)
    new_total = stripe_total
    stripe_total = round(stripe_total * 100)

    std_shipping_cost = Sitesettings.objects.get(name="Standard Shipping")
    std_value = std_shipping_cost.value
    free_ship_thres = Sitesettings.objects.get(name="Free Shipping Threshold")
    threshold_value = free_ship_thres.value
    grand_total = new_total

    # Before modifying the intent, need to take into
    # account the shipping method selected
    if request.session['shipping_cost'] != 0:
        if subtotal < threshold_value:
            stripe_total = new_total + std_value
            stripe_total = round(stripe_total * 100)
            grand_total = new_total + std_value

    # If a coupon is applied successfully, store the new
    # grand total for the cart in a session variable
    request.session['discount_total'] = float(grand_total)
    request.session['discount_subtotal'] = float(new_total)
    # Modtify the stripe payment intent to reflect the new total
    stripe.PaymentIntent.modify(
        intent_id,
        amount=stripe_total
        )

    message = "Coupon applied successfully!"
    result = {
        'message': message,
        'new_total': new_total,
        'coupon_code': coupon_code,
        'coupon_savings': coupon_savings,
        'grand_total': grand_total,
        'discount': discount,
    }

    return JsonResponse(result)

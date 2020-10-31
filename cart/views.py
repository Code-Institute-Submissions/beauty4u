from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """ A view that returns the cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add specific product to the cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity

    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    
    return redirect(redirect_url)    


def adjust_cart(request, item_id):
    """ Adjust items in the cart """
    # quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    #Just deletes item from cart for now - Need to add functionality to adjust quantity 

    del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))



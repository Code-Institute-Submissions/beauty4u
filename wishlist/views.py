from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_wishlist(request):
    """ A view that returns the cart page """
    return render(request, 'wishlist/wishlist.html')



def add_to_wishlist(request, item_id):
    """ Add product ID to list """
    redirect_url = request.POST.get('redirect_url')
    wishlist = list(request.session.get('wishlist', []))

    if item_id not in wishlist:
        #if the item id is not in the wishlist already - add it
        wishlist.append(item_id)

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)
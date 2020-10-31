from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_wishlist(request):
    """ A view that returns the cart page """
    return render(request, 'wishlist/wishlist.html')
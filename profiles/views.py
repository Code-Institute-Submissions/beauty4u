from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile 
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from django.contrib.auth.decorators import login_required
from booking.models import Bookings
import re

# Create your views here.
@login_required(login_url='/accounts/login/')
def profile(request):
    """ Render Profile View """

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Information Updated")

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
   

    context = {
        'form': form,
    }
    return render(request, "profiles/profile.html", context)

@login_required(login_url='/accounts/login/')
def my_orders(request): 

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by('-date')

    context = {
        'orders': orders
        }

    return render(request, "profiles/my_orders.html", context)



@login_required(login_url='/accounts/login/')
def my_bookings(request): 

    username = request.user.username
    bookings = Bookings.objects.filter(username=username)

    for booking in bookings:
        booking.service = re.sub(r'[^\w]', ' ', booking.service)

    context = {
        'bookings': bookings
        }

    return render(request, "profiles/my_bookings.html", context)
   
@login_required(login_url='/accounts/login/')
def view_order(request, order_number):

    order_number = order_number
    profile = get_object_or_404(UserProfile, user=request.user)
    profile_orders = profile.orders.filter(order_number=order_number)


    if profile_orders:

        order = get_object_or_404(Order, order_number=order_number)

        context = {
        'order': order, 
        }

        return render(request, "profiles/view_order.html", context)

    else:
        messages.error(request, 'Sorry, This order does not belong to you!')
        return redirect(reverse('home')) 



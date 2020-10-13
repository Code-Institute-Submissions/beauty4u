from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from .models import Bookings

""" Login Required to view this app - if not logged in - redirect to login"""
@login_required(login_url='/accounts/login/')
# Create your views here.
def booking (request):

    username = request.user.username
    bookings = Bookings.objects.all()

    new_booking = Bookings(username="dkoneill", customer_name="David O Neill", service="Blow Dry", time="3pm")
    new_booking.save()

    if not request.user.is_authenticated:
        return redirect(reverse('accounts/login'))


    queries = Q(username__icontains= request.user.username)
    bookings = bookings.filter(queries)


    context =  {
        'bookings': bookings,
        'username': username
    }
    return render(request, 'booking/booking.html', context)
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from .models import Bookings, Service_Category, Services

""" Login Required to view this app - if not logged in - redirect to login"""
@login_required(login_url='/accounts/login/')
# Create your views here.
def booking (request):
    service_type = 1
    if request.GET:
        if 'service_type' in request.GET:
            if request.GET['service_type'].isnumeric():
                service_type = request.GET['service_type']
            if not service_type:
                return redirect(reverse('booking'))

    

    username = request.user.username
    bookings = Bookings.objects.all()
    categories = Service_Category.objects.all()
    services = Services.objects.all()

    if not request.user.is_authenticated:
        return redirect(reverse('accounts/login'))

    # Filer bookings based on logged in username
    queries = Q(username__icontains= request.user.username)
    bookings = bookings.filter(queries)
    services = Services.objects.filter(service_category=service_type)

    service_type_start = 1


    """ Treat list of services to display as queries """

    context =  {
        'bookings': bookings,
        'categories': categories,
        'username': username,
        'services': services,
        'service_type_start': service_type_start
    }
    return render(request, 'booking/booking.html', context)


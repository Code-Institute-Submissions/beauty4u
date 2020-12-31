from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Bookings, serviceCategory, Services
from management.models import Staff


""" Login Required to view this app - if not logged in - redirect to login"""
@login_required(login_url='/accounts/login/')
# Create your views here.
def booking (request):
 
    username = request.user.username
    bookings = Bookings.objects.all()
    categories = serviceCategory.objects.all()
    services = Services.objects.all()

    if not request.user.is_authenticated:
        return redirect(reverse('accounts/login'))

    # Filer bookings based on logged in username
    queries = Q(username__icontains= request.user.username)
    bookings = bookings.filter(queries)
    


    """ Treat list of services to display as queries """

    context =  {
        'bookings': bookings,
        'categories': categories,
        'username': username,
        'services': services,
       
    }
    return render(request, 'booking/booking.html', context)

@require_POST
@login_required(login_url='/accounts/login/')
def select_staff(request):

    staff = Staff.objects.all()
    staff = staff.filter(available=True)

    if request.method == "POST":
        services = request.POST.getlist('displayArray[]')
        #store posted services in a django session variable
        request.session['services'] = services

       
        context = {
            'services': services,
            'staff': staff,
        }
        return render(request, 'booking/booking_staff.html', context)


@require_POST
@login_required(login_url='/accounts/login/')
def select_time(request):

    if request.method == "POST":
        return render(request, 'booking/booking_time.html')
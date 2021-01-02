from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Bookings, serviceCategory, Services
from management.models import Staff
from home.models import openHours
import json


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
        cost = request.POST.get('sessionCost')
        request.session['totalcost'] = cost

       
        context = {
            'services': services,
            'staff': staff,
        }
        return render(request, 'booking/booking_staff.html', context)


@require_POST
@login_required(login_url='/accounts/login/')
def select_time(request):

    staff_selected = request.POST.getlist('staffSelected[]')
    request.session['staff_selected'] = staff_selected

    list = []
    timeChoices = openHours.OPENING_TIME_CHOICES
    #Get days salon is open from openHours 
    open = openHours.objects.all()
    #Filter down days to the ones that are marked closed
    closed = open.filter(markedClosed=True)
    # Create Array with days the salon is closed
    for days in closed:
        if days.day == "MONDAY":
            list.append('1')
        elif days.day == "TUESDAY":
            list.append('2')
        elif days.day == "WEDNESDAY":
            list.append('3')
        elif days.day == "THURSDAY":
            list.append('4')
        elif days.day == "FRIDAY":
            list.append('5')
        elif days.day == "SATURDAY":
            list.append('6')
        elif days.day == "SUNDAY":
            list.append('7')




    # Format the array to pass to JS on frontend
    closedList = json.dumps(list)        
        
    context = {
        'listofdays': closedList,
        'time_choices': timeChoices,
    }
    if request.method == "POST":
        return render(request, 'booking/booking_time.html', context)



@require_POST
@login_required(login_url='/accounts/login/')
def confirm_booking(request):

    if request.method == "POST":
        date = request.POST.get('dateVal')
        time = request.POST.get('timeVal')
        staff =  request.session['staff_selected']
        services = request.session['services']
        cost = request.session['totalcost']
       
        context = {
            'services': services,
            'staff': staff,
            'date': date,
            'time': time,
            'cost': cost,
        }
        return render(request, 'booking/confirm_booking.html', context)

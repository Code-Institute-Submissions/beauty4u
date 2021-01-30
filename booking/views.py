from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Bookings, serviceCategory, Services
from management.models import Staff
from profiles.models import UserProfile
from home.models import openHours
import json
from django.conf import settings


@login_required(login_url='/accounts/login/')
# Create your views here.
def booking(request):

    """

    A view that will render the main booking app for the
    user to select services

    """

    username = request.user.username
    name = get_object_or_404(User, username=username)
    # Get profile of user logged in (They must have a phone number stored
    # before making a booking to ensure they can be contacted)
    profile = UserProfile.objects.get(user=name.id)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        name.first_name = first_name
        name.last_name = last_name
        profile.default_phone_number = phone_number
        name.save()
        profile.save()
        messages.info(request, 'Your details have been saved to your profile!')

    # If it is their first time booking, ask them for their name
    # and phone number
    if name.first_name is None or profile.default_phone_number is None:
        return render(request, 'booking/details.html')

    username = request.user.username
    bookings = Bookings.objects.all()
    categories = serviceCategory.objects.all()
    services = Services.objects.all()

    if not request.user.is_authenticated:
        return redirect(reverse('accounts/login'))

    # Filer bookings based on logged in username
    queries = Q(username__icontains=request.user.username)
    bookings = bookings.filter(queries)

    """ Treat list of services to display as queries """

    context = {
        'bookings': bookings,
        'service_categories': categories,
        'username': username,
        'services': services,
    }
    return render(request, 'booking/booking.html', context)


@require_POST
@login_required(login_url='/accounts/login/')
def select_staff(request):

    """
    A view that will render the select staff template for the user to select a
    staff member for their booking
    Takes posted data from booking.js

    """

    staff = Staff.objects.all()
    staff = staff.filter(available=True)

    if request.method == "POST":
        services = request.POST.getlist('displayArray[]')
        # store posted services in a django session variable
        request.session['services'] = services
        cost = request.POST.get('storeCost')
        request.session['totalcost'] = cost

        context = {
            'services': services,
            'staff': staff,
        }
        return render(request, 'booking/booking_staff.html', context)


@require_POST
@login_required(login_url='/accounts/login/')
def select_time(request):

    """

    A view that will render the select date and time template for the user to
    select a date and time for their booking
    Takes posted data from booking.js

    """

    if request.method == "POST":

        staff_selected = request.POST.getlist('staffSelected[]')
        request.session['staff_selected'] = staff_selected

        list = []
        timeChoices = openHours.OPENING_TIME_CHOICES
        # Get days salon is open from openHours
        open = openHours.objects.all()
        # Filter down days to the ones that are marked closed
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

        return render(request, 'booking/booking_time.html', context)


@require_POST
@login_required(login_url='/accounts/login/')
def confirm_booking(request):

    """
    A view that will render the confirm booking template to summarise the
    boking and ask the user to confirm
    Takes posted data from booking.js

    """

    if request.method == "POST":
        date = request.POST.get('dateVal')
        request.session['date'] = date
        time = request.POST.get('timeVal')
        request.session['time'] = time
        staff = request.session['staff_selected']
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


@require_POST
@login_required(login_url='/accounts/login/')
def booking_success(request):

    """
    A view that will process the booking, store it in the database and send
    emails to the salon owner and customer
    Takes posted data from booking.js
    """

    if request.method == "POST":

        username = request.user.username
        name = get_object_or_404(User, username=username)
        name = name.first_name + " " + name.last_name
        date = request.session['date']
        time = request.session['time']
        staff = request.session['staff_selected']
        services = request.session['services']
        cost = request.session['totalcost']

        booking = Bookings.objects.create(username=username, service=services,
                                          date=date, time=time, staff=staff,
                                          customer_name=name)
        booking.save()

        # Email
        cust_email = request.user.email
        subject = render_to_string('booking/booking_email_subject.txt')
        body = render_to_string('booking/booking_email_body.txt', {
                                'date': date,
                                'time': time, 'name': name, 'staff': staff,
                                'services': services, 'cost': cost,
                                'username': username})

        # Email to Staff
        subject2 = render_to_string('booking/booking_email_subject2.txt')
        body2 = render_to_string('booking/booking_email_body2.txt', {
                                'date': date, 'time': time, 'name': name,
                                'staff': staff, 'services': services,
                                'cost': cost, 'username': username,
                                'email': cust_email})

        # Send email to user
        send_mail(
            subject,
            body,
            "booking@beauty4u.ie",
            [cust_email],
        )

        # Send Email to Salon to notify them of booking request
        send_mail(
            subject2,
            body2,
            "booking@beauty4u.ie",
            [settings.EMAIL_HOST_USER, ],
        )

        context = {
            'services': services,
            'staff': staff,
            'date': date,
            'time': time,
            'cost': cost,

        }

        return render(request, 'booking/booking_success.html', context)

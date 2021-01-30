from django.shortcuts import (render, get_object_or_404,
                              redirect, HttpResponse, reverse)
from home.models import openHours, aboutUs
from checkout.models import Order
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from booking.models import Bookings, Services, serviceCategory
from allauth.account.models import EmailAddress
from profiles.models import UserProfile
from management.models import Sitesettings, Staff, Coupons, SiteStats
from .forms import (HoursForm, aboutForm, addProductForm, staffForm,
                    couponForm, addCategory, addBrand, updateProduct,
                    addServiceForm, addServiceCategoryForm)
from products.models import Product, Brand, Category
from django.contrib import messages
from django.db.models import Q
import datetime
from datetime import timedelta
from django.template.loader import render_to_string
from django.core.mail import send_mass_mail, send_mail
import re
from django.http import JsonResponse


# Create your views here.

def manage(request):

    """ A view that returns the dashboard home page """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a shop \
                                 owner to do this!')
        return redirect(reverse('home'))

    # Get data for website traffic
    today = datetime.date.today()
    month = today.month
    day = today.day

    last_week = today-timedelta(days=7)
    two_weeks = today-timedelta(days=14)

    next_week = today+timedelta(days=7)
    bookings = Bookings.objects.all().order_by('-date')[:5]

    for items in bookings:
        items.service = re.sub(r'[^\w]', ' ', items.service)

    recent_orders = Order.objects.all().order_by('-date')[:5]
    last_day = SiteStats.objects.filter(date__day=day).count()
    last_7 = SiteStats.objects.filter(date__lt=today,
                                      date__gt=last_week).count() + last_day
    last_31 = SiteStats.objects.filter(date__month=month).count()

    # Bookings for today
    todays_bookings = Bookings.objects.filter(date=today).count()
    # Bookings for this week
    next_7_bookings = Bookings.objects.filter(date__lt=next_week,
                                              date__gt=today,
                                              confirmed=False).count()
    this_week_bookings = Bookings.objects.filter(date__lt=next_week,
                                                 date__gt=today).count() + todays_bookings
    # Get number of website vists from 14 to 7 days ago
    # (previous week) and compare to this week
    previous_week = SiteStats.objects.filter(date__lt=last_week,
                                             date__gt=two_weeks).count()

    difference = last_7 - previous_week

    if difference < 0:
        traffic_down = 1
    else:
        traffic_down = 0

    # Get Shop Stats
    totalrevenue = 0
    orders = Order.objects.all()
    num_of_orders = Order.objects.all().count()

    for item in orders:
        totalrevenue = totalrevenue + item.total

    # Get Booking Stats
    num_of_bookings = Bookings.objects.all().count()

    # Get Total User Count (excluding super users )
    total_users = EmailAddress.objects.all().exclude(user__is_superuser=True).count()

    context = {
        'bookings': bookings,
        'recent_orders':  recent_orders,
        'orders': orders,
        'last_day': last_day,
        'last_7': last_7,
        'last_31': last_31,
        'previous_week': previous_week,
        'traffic_down': traffic_down,
        'num_of_orders': num_of_orders,
        'totalrevenue': totalrevenue,
        'num_of_bookings': num_of_bookings,
        'total_users': total_users,
        'todays_bookings': todays_bookings,
        'this_week_bookings': this_week_bookings,
        'next_7_bookings': next_7_bookings

    }

    return render(request, 'management/dashboard_home.html', context)


def view_orders(request):

    """
    A view that returns all shop orders ordered by date received

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    orders = Order.objects.all().order_by('-date')

    context = {
        'orders': orders,
    }

    return render(request, 'management/dashboard_orders.html', context)


def order_detail(request, order_number2):

    """

    A view that returns the details of an order, taking the
    order number as a parameter

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, order_number=order_number2)

    context = {
        'order': order,
    }
    return render(request, 'management/dashboard_order_detail.html', context)


def settings(request):

    """

    A view that returns the settings template
    allowing the owner to change settings on their site

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    settings = Sitesettings.objects.all()
    context = {
        'settings': settings
    }

    return render(request, 'management/dashboard_settings.html', context)


def staff(request):

    """

    A view that returns all staff members and a form
    allowing the owner to add staff members

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    form = staffForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = staffForm()
            return redirect(reverse('staff'))

    staff = Staff.objects.all()

    context = {
        'staff': staff,
        'form': form,
    }

    return render(request, 'management/dashboard_staff.html', context)


@require_POST
def save_data(request):

    """

    This view handles POST requests from the settings page
    Takes posted data from postsettings.js

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    settingName = request.POST.get('settingName')
    settingValue = request.POST.get('settingValue')
    settingStatus = request.POST.get('settingStatus')

    # Check format of setting
    setting = get_object_or_404(Sitesettings, name=settingName)
    if settingValue is not None:
        setting.value = settingValue

    if settingStatus is not None:
        setting.status = settingStatus

    setting.save()

    context = {
        'setting': settingStatus

    }

    return JsonResponse(context)


@require_POST
def update_staff_avail(request):

    """

    This view handles POST requests from the staff page and updates
    the availability of the staff member


    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    try:

        settingName = request.POST.get('settingName')
        settingStatus = request.POST.get('settingStatus')

        # Check format of setting

        setting = get_object_or_404(Staff, name=settingName)
        setting.available = settingStatus
        setting.save()

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(content=e, status=400)


@require_POST
def remove_staff(request):

    """
    A view that handles a POST request to delete a staff member

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    staff_member = request.POST.get('settingName')
    select_member = get_object_or_404(Staff, name=staff_member)
    select_member.delete()
    return HttpResponse(status=200)


@require_POST
def remove_service(request):

    """
    A view that handles a POST request to delete a service

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    service = request.POST.get('serviceName')
    select_service = get_object_or_404(Services, name=service)
    select_service.delete()
    return HttpResponse(status=200)


@require_POST
def remove_service_category(request):

    """
    A view that handles a POST request to delete a service catgory

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to \
                                 be a shop owner to do this!')
        return redirect(reverse('home'))

    service_cat = request.POST.get('servicecatName')
    select_service_cat = get_object_or_404(serviceCategory, name=service_cat)
    select_service_cat.delete()
    return HttpResponse(status=200)


def changeHours(request):

    """
    A view that will return the change hours
    template with a form allowing the user to update the opening hours

    """

    message = 0

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    if request.method == "POST":

        openHours.objects.get_or_create(day=request.POST.get("day").upper())

        instance = openHours.objects.get(day=request.POST.get("day").upper())

        form = HoursForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            form = HoursForm()
            message = 1
    else:
        form = HoursForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = HoursForm()

    hours = openHours.objects.all()

    context = {
        'hours': hours,
        'form': form,
        'message': message,
    }

    return render(request, 'management/dashboard_changehours.html', context)


def changeAbout(request):

    """
    A view that will return the change about us template and a
    form allowing the user to change the about us text
    displayed on the home page

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    text = aboutUs.objects.get(pk=1)
    form = aboutForm(request.POST or None, instance=text)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            messages.info(request, 'About Text Updated!')
            form = aboutForm()

    context = {
        'form': form,
        'text': text,
    }

    return render(request, 'management/changeAbout.html', context)


def coupons(request):

    """
    A view that will display all coupons and a form allowing
    the user to add a new coupon

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to \
                                 be a shop owner to do this!')
        return redirect(reverse('home'))

    form_error = False
    coupons = Coupons.objects.all()
    count = coupons.count()
    form = couponForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            form = couponForm()
            form_error = False
            return redirect(reverse('coupons'))
        else:
            form_error = True

    context = {
        'coupons': coupons,
        'count': count,
        'form': form,
        'form_error': form_error,
    }

    return render(request, 'management/dashboard_coupons.html',  context)


@require_POST
def update_coupon_minspend(request):

    """
    This view handles POST requests
    from postsettings.js
    It allows the customer to update the
    minimum spend setting on a selected coupon

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to \
                                 be a shop owner to do this!')
        return redirect(reverse('home'))
    try:

        minspend = request.POST.get('minspend')
        couponName = request.POST.get('couponName')

        # Check format of setting
        coupon = get_object_or_404(Coupons, code=couponName)
        coupon.minspend = minspend
        coupon.save()

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(content=e, status=400)


@require_POST
def update_coupon_active(request):

    """
    This view handles POST requests
    from postsettings.js
    It allows the customer to update the active status on a coupon

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    try:
        """ This view will handle Post requests from the settings page """
        settingName = request.POST.get('settingName')
        settingStatus = request.POST.get('settingStatus')

        # Check format of setting
        setting = get_object_or_404(Coupons, code=settingName)
        setting.active = settingStatus
        setting.save()

        return HttpResponse(status=200)

    except Exception as e:

        return HttpResponse(content=e, status=400)


def manage_products(request):

    """

    A view that returns all products to the template
    and allows users to filter products

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    if 'brand' in request.GET:
        query = request.GET['brand']
        products = products.filter(brand__brand=query)

    if 'category' in request.GET:
        query = request.GET['category']
        products = products.filter(category__name=query)

    context = {
        'products': products,
        'query': query,
        'brands': brands,
        'categories': categories,
    }

    return render(request, 'management/dashboard_manage_products.html',
                  context)


def add_a_product(request):

    """

    A view that returns a form allowing users to
    add a product to the store

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    message = ""
    messageresult = 0

    if request.method == "POST":
        form = addProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            message = "Product Added Successfully"
            messageresult = 1
        else:
            message = "Opps! Something went wrong!"
            messageresult = 2

    form = addProductForm()

    context = {
        'form': form,
        'message': message,
        'messageresult': messageresult,
    }

    return render(request, "management/dashboard_add_product.html", context)


@require_POST
def delete_product(request):

    """

    A view that takes POSt request from postsettings.js and deletes a product

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    product_name = request.POST.get('product_name')

    product = Product.objects.filter(name=product_name)
    product.delete()

    return HttpResponse(status=200)


def manage_specific_product(request, product_name):

    """

    A view that returns a prefilled form with a product
    allowing the user to alter details of that product

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))

    message = ""
    messageresult = 0

    product = get_object_or_404(Product, name=product_name)
    if request.method == "POST":
        form = updateProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            message = "Product Updated Successfully"
            messageresult = 1
        else:
            message = "Opps! Something went wrong!"
            messageresult = 2

    form = updateProduct(instance=product)

    if not product:
        messages.error(request, 'Sorry, No products make your query!')
        return redirect(reverse('home'))

    context = {
        'product_name': product_name,
        'form': form,
        'message': message,
        'messageresult': messageresult,
    }

    return render(request, "management/dashboard_manage_specific_product.html",
                  context)


def add_a_category(request):

    """
    A view the returns all categories and a form allowing
    the user to create a category

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    form = addCategory(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = addCategory()

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, "management/dashboard_add_category.html", context)


def add_a_brand(request):

    """
    A view the returns all brands and a form allowing
    the user to create a brand

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    form = addBrand(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = addBrand()

    brands = Brand.objects.all()

    context = {
        'brands': brands,
        'form': form,
    }

    return render(request, "management/dashboard_add_brand.html",
                  context)


@require_POST
def delete_a_brand(request):

    """
    A view that thakes POST requests from postsettings.js
    and deletes the selected brand

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    brand_name = request.POST.get('brand_name')

    brand = Brand.objects.filter(brand=brand_name)
    brand.delete()

    return HttpResponse(status=200)


@require_POST
def delete_a_category(request):

    """
    A view that thakes POST requests from postsettings.js
    and deletes the selected category

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    category_name = request.POST.get('category_name')

    category = Category.objects.filter(name=category_name)
    category.delete()

    return HttpResponse(status=200)


def bookings(request):

    """
    A view that returns all bookings

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    # Get all bookings and order by latest first
    bookings = Bookings.objects.all().order_by('-date')

    context = {
        'bookings': bookings,
    }

    return render(request, 'management/dashboard_bookings.html',  context)


@require_POST
def update_booking_status(request):

    """
    A view to handle post requests from the confirm booking toggler
    Sends an email to the customer to say their booking has been
    confirmed with the toggler is clicked

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    customer_name = request.POST.get('customerName')
    confirmed = request.POST.get('confirmBooking')
    date_string = request.POST.get('bookingDate')
    time = request.POST.get('bookingTime')
    booking_id = request.POST.get('bookingId')

    customer_name_string = str(customer_name).strip()
    booking_date_string = str(date_string).strip()
    booking_time_string = str(time).strip()

    customer_booking = get_object_or_404(Bookings, booking_id=booking_id)
    customer_booking.confirmed = confirmed
    username = customer_booking.username
    customer_booking.save()

    confirmedStatus = customer_booking.confirmed

    user = get_object_or_404(User, username=username)
    email = user.email

    # Email
    cust_email = email
    subject = render_to_string('booking/confirm_booking_subject.txt')
    body = render_to_string('booking/confirm_booking_body.txt',
                            {'date': booking_date_string,
                             'time': booking_time_string,
                             'name': customer_name_string})

    # Send email to user to say booking was confirmed
    send_mail(
        subject,
        body,
        "booking@beauty4u.ie",
        [cust_email],
        )

    booking_id = {
        'booking_id': booking_id,
        'confirmedStatus': confirmedStatus,
    }

    return JsonResponse(booking_id)


def clear_bookings(request):

    """
    A view that clears all unconfirmed bookings

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    # Get all bookings and order by latest first
    bookings = Bookings.objects.all().order_by('-date')

    for booking in bookings:
        if not booking.confirmed:
            booking.delete()

    bookings = Bookings.objects.all().order_by('-date')

    context = {
        'bookings': bookings,
    }

    return render(request, 'management/dashboard_bookings.html',  context)

    return render(request, 'management/dashboard_bookings.html',
                  context)


def view_booking_details(request, booking_id):

    """

    A view that returns the details of the booking

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be \
                                 a shop owner to do this!')
        return redirect(reverse('home'))

    # Get the booking
    booking = Bookings.objects.get(id=booking_id)
    booking.service = re.sub(r'[^\w]', ' ', booking.service)

    # Get the customer details
    customer = User.objects.get(username=booking.username)
    profile = UserProfile.objects.get(user=customer.id)
    # Strip phone number of spaces for use in html link
    if profile.default_phone_number:
        profile.default_phone_number.replace(" ", "")

    context = {
        'booking': booking,
        'customer': customer,
        'profile': profile
    }

    return render(request, 'management/dashboard_booking_details.html',
                  context)


def send_marketing_email(request):

    """

    A view that returns a template allowing the user to send
    an email to all users that are not superusers

    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You need to be a \
                                 shop owner to do this!')
        return redirect(reverse('home'))
    # Get emails (exclude blank email instances and staff)
    emails = User.objects.all().exclude(is_staff=True)
    emails = emails.values('email').exclude(email="", )
    num_of_emails = emails.count()

    # Extract list of emails
    list_of_emails = []
    for users in emails:
        for values in users.values():
            list_of_emails.append(values)

    success = 0
    if request.method == "POST":

        # Get all emails
        email_subject = request.POST.get('email_subject')
        email_body = request.POST.get('email_content')

        # Open connection to gmail to send emails - use send_mass_email
        # for efficiency to only open one connection
        try:
            # Create individual instances so that email list is
            # not shared with all
            message = [(email_subject, email_body, "marketing@beauty4u.ie",
                        [email]) for email in list_of_emails]
            send_mass_mail(message)
            success = 1

        except Exception:
            success = 2

    context = {
        'num_of_emails': num_of_emails,
        'success': success,
    }

    return render(request, "management/dashboard_marketing.html", context)


def addService(request):

    """
    A view that returns all services and a form allowing
    the user to add a service

    """

    services = Services.objects.all()

    form = addServiceForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            form = addServiceForm()

    context = {
        'services': services,
        'form': form,
    }

    return render(request, "management/dashboard_addservice.html", context)


def addServiceCategory(request):

    """
    A view that returns all service categories and a form
    allowing the user to add a service category

    """

    categories = serviceCategory.objects.all()

    form = addServiceCategoryForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            form = addServiceCategoryForm()

    context = {
        'categories': categories,
        'form': form,

    }

    return render(request, "management/dashboard_addservicecat.html", context)

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from home.models import openHours, aboutUs
from django.views.decorators.http import require_POST
from booking.models import Bookings
from checkout.models import Order, OrderLineItem
from allauth.account.models import EmailAddress
from management.models import Sitesettings, Staff, Coupons, SiteStats
from .forms import HoursForm, aboutForm, addProductForm, staffForm, couponForm
from products.models import Product, Brand, Category
from django.contrib import messages
from decimal import Decimal
from django.db.models import Q
import datetime
from datetime import timedelta


# Create your views here.

def manage(request):
    """ A view that returns the dashboard home page """

    #Get data for website traffic 
    today = datetime.date.today()
    month = today.month
    day = today.day
    last_week = today-timedelta(days=7)
    two_weeks = today-timedelta(days=14)

   
    bookings = Bookings.objects.all().order_by('-date')[:5] 
    orders = Order.objects.all().order_by('-date')[:5]

    last_day = SiteStats.objects.filter(date__day=day).count()
    last_7 = SiteStats.objects.filter(date__lt=today, date__gt=last_week).count() + last_day
    last_31 = SiteStats.objects.filter(date__month=month).count()

    # Get number of website vists from 14 to 7 days ago (previous week) anfd compare to this week
    previous_week = SiteStats.objects.filter(date__lt=last_week, date__gt=two_weeks).count()

    difference = last_7 - previous_week

    if difference < 0:
        traffic_down = 1
    else:
        traffic_down = 0    

    #Get Shop Stats
    totalrevenue = 0
    orders = Order.objects.all()
    num_of_orders = Order.objects.all().count() 

    for item in orders:
        totalrevenue = totalrevenue + item.total 

    #Get Booking Stats
    num_of_bookings = Bookings.objects.all().count() 

    #Get Total User Count (excluding super users )
    total_users = EmailAddress.objects.all().exclude(user__is_superuser=True).count()

    context = {
        'bookings': bookings,
        'orders': orders,
        'last_day': last_day,
        'last_7': last_7,
        'last_31': last_31,
        'previous_week': previous_week,
        'traffic_down': traffic_down,
        'num_of_orders': num_of_orders,
        'totalrevenue': totalrevenue,
        'num_of_bookings': num_of_bookings,
        'total_users': total_users

    }

    return render(request, 'management/dashboard_home.html', context)


def view_orders(request):
    
    orders = Order.objects.all().order_by('-date')

    context = {
        'orders': orders,
    }

    return render(request, 'management/dashboard_orders.html', context)


def order_detail(request, order_number2):

    order = get_object_or_404(Order, order_number=order_number2)

    context = {
        'order': order,
    }
    return render(request, 'management/dashboard_order_detail.html', context)






def settings(request):

    settings = Sitesettings.objects.all()
    context = {
        'settings': settings
    }

    return render(request, 'management/dashboard_settings.html', context)



def staff(request):

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

    """ This view will handle Post requests from the settings page """
    settingName = request.POST.get('settingName')
    settingValue = request.POST.get('settingValue')
    settingStatus= request.POST.get('settingStatus')

    # Check format of setting 

    setting = get_object_or_404(Sitesettings, name=settingName)
    if settingValue is not None:
        setting.value = settingValue
    
    if settingStatus is not None:
        setting.status = settingStatus
            
    setting.save()
    print(f'New Status: {setting.status}')

    return HttpResponse(status=200)



@require_POST
def update_staff_avail(request):
    try:
        """ This view will handle Post requests from the settings page """
        settingName = request.POST.get('settingName')
        settingStatus= request.POST.get('settingStatus')

        # Check format of setting 

        setting = get_object_or_404(Staff, name=settingName)

        setting.available = settingStatus
                
        setting.save()
        print(f'New Status: {setting.available}')

        return HttpResponse(status=200)
    
    except Exception as e:
        print(e)
        return HttpResponse(content=e, status=400)


@require_POST
def remove_staff(request):
    staff_member = request.POST.get('settingName')
    select_member = get_object_or_404(Staff, name=staff_member)
    select_member.delete()
    return HttpResponse(status=200)  



def changeHours(request):

    if request.method == "POST":
  
        openHours.objects.get_or_create(day=request.POST.get("day").upper())

        instance = openHours.objects.get(day=request.POST.get("day").upper())

        form = HoursForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.info(request, 'Opening Hours Updated!')
            form = HoursForm()
                 

    else:
        form = HoursForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, 'Opening Hours Updated!')
            form = HoursForm()



    """ A view that returns the page to enter opening hours """
    hours = openHours.objects.all()

    context = {
    'hours': hours,
    'form': form,
    }

    """ A view that returns the index page """
    return render(request, 'management/changehours.html', context)


def changeAbout(request):

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

    """ A view that returns the index page """
    return render(request, 'management/changeAbout.html', context)


def add_a_product(request):

    form = addProductForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'Product Added!')
            form = addProductForm()

    context = {
        'form': form, 
    }

    """ A view that returns the index page """
    return render(request, 'management/addProduct.html',  context)


def coupons(request):

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

    """ A view that returns the coupon page """
    return render(request, 'management/dashboard_coupons.html',  context)

@require_POST
def update_coupon_minspend(request):
    try:
        """ This view will handle Post requests from the settings page """
        minspend = request.POST.get('minspend')
        couponName = request.POST.get('couponName')
        # Check format of setting 

        coupon = get_object_or_404(Coupons, code=couponName)
        coupon.minspend = minspend
        coupon.save()
        print(f'New Status: {coupon.minspend}')

        return HttpResponse(status=200)
    
    except Exception as e:
        print(e)
        return HttpResponse(content=e, status=400)


@require_POST
def update_coupon_active(request):
    try:
        """ This view will handle Post requests from the settings page """
        settingName = request.POST.get('settingName')
        settingStatus= request.POST.get('settingStatus')

        # Check format of setting 

        setting = get_object_or_404(Coupons, code=settingName)

        setting.active = settingStatus
                
        setting.save()
        print(f'New Status: {setting.active}')

        return HttpResponse(status=200)
    
    except Exception as e:
        print(e)
        return HttpResponse(content=e, status=400)




def manage_products(request):

    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q'] 
        print(query)
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    if 'brand' in request.GET:
        query = request.GET['brand'] 
        print(query)
        products = products.filter(brand__brand=query)


    if 'category' in request.GET:
        query = request.GET['category'] 
        print(query)
        products = products.filter(category__name=query)


    context = {
        'products': products,
        'query': query,
        'brands': brands,
        'categories': categories,
    }

    """ A view that returns the product management page """
    return render(request, 'management/dashboard_manage_products.html',  context)
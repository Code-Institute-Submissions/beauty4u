from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from home.models import openHours, aboutUs
from django.views.decorators.http import require_POST
from booking.models import Bookings
from checkout.models import Order, OrderLineItem
from management.models import Sitesettings, Staff, Coupons
from .forms import HoursForm, aboutForm, addProductForm, staffForm, couponForm
from products.models import Product, Brand, Category
from django.contrib import messages
from decimal import Decimal
from django.db.models import Q


# Create your views here.

def manage(request):
    """ A view that returns the dashboard home page """
    bookings = Bookings.objects.all().order_by('-date')[:5] 
    orders = Order.objects.all().order_by('-date')[:5]

    # Get Unique Website Visits


    context = {
        'bookings': bookings,
        'orders': orders
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
            messages.info(request, 'Staff Member Added')
            form = staffForm()
        

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
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from home.models import openHours, aboutUs
from django.views.decorators.http import require_POST
from booking.models import Bookings
from checkout.models import Order
from management.models import Sitesettings, Staff
from .forms import HoursForm, aboutForm, addProductForm
from django.contrib import messages
from decimal import Decimal


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


def settings(request):

    settings = Sitesettings.objects.all()
    

    context = {
        'settings': settings
    }

    return render(request, 'management/dashboard_settings.html', context)



def staff(request):

    staff = Staff.objects.all()

    context = {
        'staff': staff
    }

    return render(request, 'management/dashboard_staff.html', context)    

@require_POST
def save_data(request):
    try:
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
    
    except Exception as e:
        print(e)
        return HttpResponse(content=e, status=400)

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
        print(f'New Status: {setting.availability}')

        return HttpResponse(status=200)
    
    except Exception as e:
        print(e)
        return HttpResponse(content=e, status=400)





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
    if form.is_valid():
        form.save()
        messages.info(request, 'Product Added!')
        form = addProductForm()

    context = {
        'form': form, 
    }

    """ A view that returns the index page """
    return render(request, 'management/addProduct.html',  context)
from django.shortcuts import render, get_object_or_404
from home.models import openHours, aboutUs
from .forms import HoursForm, aboutForm, addProductForm
from django.contrib import messages


# Create your views here.

def manage(request):
    """ A view that returns the index page """
    return render(request, 'management/index.html')

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
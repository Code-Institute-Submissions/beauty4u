from django.shortcuts import render
from .models import openHours, aboutUs
from django.conf import settings
# Create your views here.

def index(request):
    print(settings.BASE_DIR)
    hours = openHours.objects.all()
    text = aboutUs.objects.all()

    context = {
    'text': text,    
    'hours': hours,
    }

    """ A view that returns the index page """
    return render(request, 'home/index.html', context)
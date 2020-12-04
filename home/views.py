from django.shortcuts import render
from .models import openHours
# Create your views here.

def index(request):
    hours = openHours.objects.all()



    context = {
    'hours': hours
    }

    """ A view that returns the index page """
    return render(request, 'home/index.html', context)
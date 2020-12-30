from django.shortcuts import render, get_object_or_404
from .models import openHours, aboutUs
from management.models import SiteStats
from django.conf import settings
import datetime
import calendar

# Create your views here.

def index(request):
    #Start a session to register website visit for stats 
    if 'homevisit' in request.session:
        print ("session exists")
    else:
        request.session['homevisit'] = "1"
        #Create a new visit record if session was not found
        current_date = datetime.date.today()
        current_day = datetime.datetime.today()
        current_day = calendar.day_name[current_day.weekday()] 
        SiteStats.objects.create(date=current_date, day=current_day)
        print("Visit Recorded")
    

    hours = openHours.objects.all()
    text = aboutUs.objects.all()

    context = {
    'text': text,    
    'hours': hours,
    }

    """ A view that returns the index page """
    return render(request, 'home/index.html', context)
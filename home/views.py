from django.shortcuts import render, get_object_or_404
from .models import openHours, aboutUs
from management.models import SiteStats
from django.conf import settings
import datetime
import calendar
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings


def index(request):

    """
    A view to render the home page template 
    Registers unique site visit for stats 

    """

    #Start a session to register website visit for stats 
    if 'homevisit' not in request.session:
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



def contact(request):

    """
    A view that returns the contact us page and takes posted information from contact.js

    """

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        send_to_email = settings.EMAIL_HOST_USER
        subject = render_to_string('home/contact_subject.txt')
        body = render_to_string('home/contact_body.txt', {'name': name, 'email': email, 'message': message})


        try:
            #Send email to site owner
            send_mail(
                subject, 
                body, 
                "contact@beauty4u.ie",
                [send_to_email],
            )
            result = "Thank you for contacting us! We'll be in touch soon."
            result_class = "alert-success"
        except:
            result = "There was a problem sending your email! Please try again later."
            result_class = "alert-warning"

        data = {
            'result': result, 
            'result_class': result_class
            }
        return JsonResponse(data)   

    return render(request, 'home/contact.html')



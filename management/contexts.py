from django.shortcuts import get_object_or_404
from .models import Sitesettings
from home.models import openHours


""" This context file will allow all pages to access the site settings """


def setting_contents(request):

    # opening hours
    hours = openHours.objects.all()

    # Free Shipping
    free_shipping = get_object_or_404(Sitesettings,
                                      name="Free Shipping Threshold")
    free_shipping_setting = free_shipping.status
    free_shipping_threshold = free_shipping.value

    # Standard Shipping Cost
    standard_shipping = get_object_or_404(Sitesettings,
                                          name="Standard Shipping")
    standard_shipping_setting = standard_shipping.status
    standard_shipping_cost = standard_shipping.value

    context = {
        'free_shipping_setting': free_shipping_setting,
        'free_shipping_threshold': free_shipping_threshold,
        'standard_shipping_setting': standard_shipping_setting,
        'standard_shipping_cost': standard_shipping_cost,
        'hours': hours
    }

    return context

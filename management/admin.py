from django.contrib import admin
from .models import Sitesettings, Staff, Coupons, SiteStats


class StatsAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'day',
    )


# Register your models here.
admin.site.register(Sitesettings)
admin.site.register(SiteStats, StatsAdmin)
admin.site.register(Staff)
admin.site.register(Coupons)

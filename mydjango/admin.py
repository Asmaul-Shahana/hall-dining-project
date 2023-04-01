from django.contrib import admin
from mydjango.models import Breakfast, Lunch, Snacks, Dinner, Booking, Events
# Register your models here.
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Snacks)
admin.site.register(Dinner)
admin.site.register(Booking)
admin.site.register(Events)

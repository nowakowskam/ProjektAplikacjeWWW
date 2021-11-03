from django.contrib import admin

# Register your models here.
from .models import AdditionalService, Reservation,Room,Order

admin.site.register(AdditionalService)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Order)
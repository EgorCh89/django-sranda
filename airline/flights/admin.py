from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Airport)
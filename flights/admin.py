from django.contrib import admin
from .models import Passenger
from .models import Flight

#Admin panel 

#Built-in Django Admin interface using the model created
admin.site.register(Flight)
admin.site.register(Passenger)
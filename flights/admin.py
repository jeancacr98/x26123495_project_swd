from django.contrib import admin
from .models import Passenger

#Admin panel 

#Built-in Django Admin interface using the model created
admin.site.register(Passenger)
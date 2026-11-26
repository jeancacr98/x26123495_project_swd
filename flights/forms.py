# Forms for the flights application
from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    #Create/update passenger info
    class Meta:
        model = Passenger
        fields = ['full_name', 'flight_number', 'seat_number', 'status']
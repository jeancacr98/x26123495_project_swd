from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Passenger

#Viewa for the flights
#To access the dashboard it is necessary the login
@login_required
def dashboard(request):
    #List of all the passengers
    passengers = Passenger.objects.all()
    return render(request, 'pages/dashboard.html', {'passengers': passengers})
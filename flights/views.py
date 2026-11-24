from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Passenger

@login_required
def dashboard(request):
    passengers = Passenger.objects.all()
    return render(request, 'pages/dashboard.html', {'passengers': passengers})
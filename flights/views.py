#Views for the flights application
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from .models import Passenger
from .forms import PassengerForm


@login_required
def dashboard(request):
    search_query = request.GET.get('q', '').strip()
    
    if search_query:
        passengers = Passenger.objects.select_related('flight').filter(
            full_name__icontains=search_query
        )
    else:
        passengers = Passenger.objects.select_related('flight').all()
        
    return render(request, 'pages/dashboard.html', {
        'passengers': passengers,
        'search_query': search_query
    })


#Login and permission to create a new passenger
@login_required
@permission_required('flights.add_passenger', raise_exception=True)
def passenger_create(request):
    #Allows to register a new passenger, except Auditor
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PassengerForm()
    
    return render(request, 'pages/passenger_form.html', {
        'form': form,
        'title': 'Add New Passenger'
    })

#Login and permission to update a passenger
@login_required
@permission_required('flights.change_passenger', raise_exception=True)
def passenger_update(request, pk):
    #Allows to update a passenger, except Auditor
    passenger = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PassengerForm(instance=passenger)
        
    return render(request, 'pages/passenger_form.html', {
        'form': form,
        'title': f'Edit Passenger: {passenger.full_name}'
    })

#Login and permission to delete a passenger
@login_required
@require_POST
@permission_required('flights.delete_passenger', raise_exception=True)
def passenger_delete(request, pk):
     #Allows to delete a passenger, except Auditor and Agent
    passenger = get_object_or_404(Passenger, pk=pk)
    passenger.delete()
    return redirect('dashboard')
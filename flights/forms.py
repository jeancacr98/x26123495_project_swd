from django import forms
from .models import Passenger


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['flight', 'full_name', 'seat_number', 'status']
        widgets = {
            'flight': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., John Doe'}),
            'seat_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 14B'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
from django.db import models
from django.core.validators import RegexValidator

class Passenger (models.Model):
    #Predefined status
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Boarded', 'Boarded'),
        ('Cancelled', 'Cancelled'),
    ]

    letters_validator = RegexValidator(
        regex=r'^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$',
        message='Only letters and spaces are allowed. No special characters or numbers.'
    )

    alphanumeric_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9]+$',
        message='Only letters and numbers are allowed. No special characters, symbols, or spaces.'
    )

    #Inputs with max length, one input with options
    full_name = models.CharField(max_length=30, validators=[letters_validator])
    flight_number = models.CharField(max_length=5, validators=[alphanumeric_validator])
    seat_number = models.CharField(max_length=3, validators=[alphanumeric_validator])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    #Passenger info String
    def __str__(self):
        return f"{self.full_name} - {self.flight_number} ({self.seat_number})"
from django.db import models
from django.core.validators import RegexValidator

# Database models for the flights application.
class Passenger (models.Model):
    
    #Predefined status to prevent string injection
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Boarded', 'Boarded'),
        ('Cancelled', 'Cancelled'),
    ]

    #Input Sanitization, no special characters or numbers
    letters_validator = RegexValidator(
        regex=r'^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$',
        message='Only letters and spaces are allowed. No special characters or numbers.'
    )

    #Input Sanitization, no special characters, symbols, or spaces
    alphanumeric_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9]+$',
        message='Only letters and numbers are allowed. No special characters, symbols, or spaces.'
    )

    #Passenger inputs with max length, one input with options applying the validators created
    full_name = models.CharField(max_length=30, validators=[letters_validator])
    flight_number = models.CharField(max_length=5, validators=[alphanumeric_validator])
    seat_number = models.CharField(max_length=3, validators=[alphanumeric_validator])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    #Passenger info string
    def __str__(self):
        return f"{self.full_name} - {self.flight_number} ({self.seat_number})"
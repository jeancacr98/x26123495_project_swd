from django.db import models
from django.core.validators import RegexValidator

#INPUT SANITIZATION
#Validate only letters
LETTERS_VALIDATOR = RegexValidator(
    regex=r'^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$',
    message='Only letters and spaces are allowed. No special characters or numbers.'
)

#Validate letters and numbers
ALPHANUMERIC_VALIDATOR = RegexValidator(
    regex=r'^[a-zA-Z0-9]+$',
    message='Only letters and numbers are allowed. No special characters, symbols, or spaces.'
)

class Flight(models.Model):
    flight_number = models.CharField(
        max_length=20,
        unique=True,
        validators=[ALPHANUMERIC_VALIDATOR],
        help_text="Unique alphanumeric flight code (e.g., EI105)."
    )
    origin = models.CharField(
        max_length=100,
        validators=[LETTERS_VALIDATOR],
        help_text="Departure city (e.g., Dublin)."
    )
    destination = models.CharField(
        max_length=100,
        validators=[LETTERS_VALIDATOR],
        help_text="Arrival city (e.g., Madrid)."
    )
    departure_date = models.DateField(
        help_text="Scheduled departure date."
    )

    def __str__(self):
        return f"{self.flight_number} ({self.origin} -> {self.destination})"


class Passenger(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Boarded', 'Boarded'),
        ('Cancelled', 'Cancelled'),
    ]

    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name='passengers',
        help_text="Select the assigned flight."
    )
    full_name = models.CharField(
        max_length=150,
        validators=[LETTERS_VALIDATOR],
        help_text="Passenger's full legal name."
    )
    seat_number = models.CharField(
        max_length=10,
        validators=[ALPHANUMERIC_VALIDATOR],
        help_text="Assigned seat code (e.g., 14B)."
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
        help_text="Current boarding status of the passenger."
    )

    def __str__(self):
        return f"{self.full_name} - {self.flight.flight_number} ({self.seat_number})"
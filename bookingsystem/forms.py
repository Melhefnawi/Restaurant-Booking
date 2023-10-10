from .models import Booking_details
from django import forms


class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking_details
        field = ('First_Name', 'Last_Name', 'Date', 'Time', 'People_No',)

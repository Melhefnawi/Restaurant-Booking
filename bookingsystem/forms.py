from .models import Booking_details
from django import forms


class BookingForms(forms.ModelForm):

    class Meta:

        model = Booking_details
        fields = ('First_Name', 'Last_Name', 'Date',
                  'Time', 'Phone_Number', 'People_No', 'Email', )

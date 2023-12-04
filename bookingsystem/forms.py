from .models import Booking_details
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# Creating the Booking_Form 


class BookingForms(forms.ModelForm):

    class Meta:

        model = Booking_details
        fields = ('First_Name', 'Last_Name', 'Date',
                  'Time', 'Phone_Number', 'People_No', 'Email', )
        widgets = {
            'Date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }        



       

from .models import Booking_details
from django import forms
from crispy_forms.helper import FormHelper
from django.utils.timezone import now
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# Creating the Booking_Form 

class FutureDateInput(forms.DateInput):
    input_type = 'date'

    def get_context(self, name, value, attrs):
        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)


class BookingForms(forms.ModelForm):

    class Meta:

        model = Booking_details
        fields = ('First_Name', 'Last_Name', 'Date',
                  'Time', 'Phone_Number', 'People_No', 'Email', )
        widgets = {
            'Date' : FutureDateInput(),
            'Time': forms.DateInput(
                format=("%H:%M"),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'time'  
                      }),
            'Phone_Number' : forms.NumberInput(attrs={'type' :'number'}),
            'People_No' : forms.NumberInput(attrs={'type' :'number'}),
            'Email': forms.EmailInput(attrs = {'type':'email'}),

                
        }        






            
       

from .models import Booking_details
from django import forms
from crispy_forms.helper import FormHelper
from django.utils.timezone import now
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from phonenumber_field.widgets import PhoneNumberPrefixWidget    

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
            #'Phone_Number': PhoneNumberPrefixWidget(),
            "Phone_Number": forms.TextInput(
                attrs={
                    "placeholder": "Phone number (with a country code) ",
                    "type": "tel",
                    "minlength": 12,
                    "maxlength": 15,}),
            'Date' : FutureDateInput(),
            'Time': forms.DateInput(
                format=("%H:%M"),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'time'  
                    }),
            

                
         }        






            
    

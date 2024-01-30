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
        fields = ( 'User','First_Name', 'Last_Name','Email','Date',
                  'Time', 'Phone_Number', 'People_No',)
        widgets = {
            #'Phone_Number_0': PhoneNumberPrefixWidget(initial='IE'),
            "Phone_Number": forms.TextInput(attrs={
                  "placeholder": "Phone number (without a country code or any sign) ",
                  "type": "tel",}),
                 # "minlength": 5,
                 #   "maxlength": 15,}),
            'User' : forms.HiddenInput(),  
            'Date' : FutureDateInput(),
            'Time': forms.DateInput(
                format=("%H:%M"),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'time'  
                    }),
            

                
         }        






            
    

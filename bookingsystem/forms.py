from .models import Booking_details
from django import forms
from crispy_forms.helper import FormHelper
from django.utils.timezone import now
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from phonenumber_field.widgets import PhoneNumberPrefixWidget  
from datetime import datetime, timedelta  

# Creating the Booking_Form 

#class FutureDateInput(forms.DateInput):
#    input_type = 'date'

#    def get_context(self, name, value, attrs):
#        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
#        return super().get_context(name, value, attrs)

class FutureDateInput(forms.DateInput):
    input_type = 'date'

    def get_context(self, name, value, attrs):
        current_date = datetime.now().date()
        one_day_later = current_date + timedelta(days=1)
        attrs.setdefault('min', one_day_later.strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)

class CurrentOrOneHourLaterTimeField(forms.TimeField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_time = datetime.now()
        one_hour_later = current_time + timedelta(hours=1)
        time_value = one_hour_later.strftime('%H:%M')  # Format as HH:MM
        self.initial = time_value

class BookingForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Calculate current time and one hour later
        current_time = datetime.now().time()
        one_hour_later = (datetime.now() + timedelta(hours=1)).time()

        # Format the times as string in 'HH:MM' format
        current_time_str = current_time.strftime('%H:%M')
        one_hour_later_str = one_hour_later.strftime('%H:%M')

        # Set the initial value of the time field
        self.fields['Time'] = forms.TimeField(
            initial=one_hour_later_str,
            widget=forms.TimeInput(
                format='%H:%M',
                attrs={
                    'class': 'form-control',
                    
                    'type': 'time',
                    #'min': current_time_str,
                    'id': 'id_time_field', 
                }
            )
        )

  

    class Meta:

        model = Booking_details
        fields = ('User','Date',
                  'Time', 'Phone_Number', 'People_No',)
        widgets = {
            #'Phone_Number_0': PhoneNumberPrefixWidget(initial='IE'),
            "Phone_Number": forms.TextInput(attrs={
                  "placeholder": "Please enter a 10-digit number without spaces or characters.",
                  "type": "tel",}),
                 # "minlength": 5,
                 #   "maxlength": 15,}),
            'User' : forms.HiddenInput(),  
            'Date' : FutureDateInput(),
            #'Time': forms.DateInput(
            #        format=("%H:%M"),
            #    attrs={'class': 'form-control', 
            #           'placeholder': 'Select a date',
            #           'type': 'time'  
            #       })
            #'Time': CurrentOrOneHourLaterTimeField(widget=forms.TimeInput(
            #        format=("%H:%M"),
            #        attrs={'class': 'form-control', 
            #               'placeholder': 'Select a time',
            #               'type': 'time'  
            #           })),
           
            
        
                
         }        






            
    

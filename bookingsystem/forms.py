from .models import Booking_details
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


class BookingForms(forms.ModelForm):

    class Meta:

        model = Booking_details
        fields = ('First_Name', 'Last_Name', 'Date',
                  'Time', 'Phone_Number', 'People_No', 'Email', )


class Pre_Booking(forms.ModelForm):

    class Meta:
          
        model = Booking_details
        fields = ('First_Name', 'Last_Name', 'Phone_Number', )
       

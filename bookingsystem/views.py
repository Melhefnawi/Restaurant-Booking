from django.shortcuts import render
from django.views import generic
from .models import Booking_details, Client, Menu
# Create your views here.


class BookingList(generic.ListView):

    model = Booking_details
    queryset = Booking_details.objects.all()
    template_name = 'booking/index.html'



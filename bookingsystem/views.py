from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, view
from .models import Booking_details, Client, Menu
# Create your views here.


class BookingList(generic.ListView):

    model = Booking_details
    queryset = Booking_details.objects.all()
    template_name = 'booking/index.html'


class BookingDetails(view):

    def get(self, request, First_Name, *args, **kwargs):

        queryset = Booking_details.objects.all()
        booking = get_object_or_404(queryset, First_Name=First_Name)


from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking_details, Client, Menu
from .forms import BookingForms
# Create your views here.


class BookingList(generic.ListView):

    model = Booking_details
    queryset = Booking_details.objects.all()
    template_name = 'booking/index.html'


class BookingDetails(View):

    def get(self, request, First_Name, *args, **kwargs):

        queryset = Booking_details.objects.all()
        booking = get_object_or_404(queryset, First_Name=First_Name)

        return render(request, "booking/booking_details.html",
                      {"booking": booking, "booking_form": BookingForms()})

    def post(self, request, First_Name, *args, **kwargs):

        booking_form = BookingForms(request.POST)

        if booking_form.is_valid():
            booking_form.save()
        else:
            booking_form = BookingForms()
        return render(request, "booking/booking_details.html", {
                                                            "booking_form": BookingForms()})

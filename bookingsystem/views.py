from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic, View
from .models import Booking_details, Client, Menu
from .forms import BookingForms
from random import *
# Create your views here.


class BookingList(generic.ListView):

    model = Booking_details
    queryset = Booking_details.objects.all()
    template_name = 'booking/index.html'


class MenuList(generic.ListView):

    model = Menu
    queryset = Menu.objects.all()
    template_name = 'booking/menu.html'


class BookingDetails(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Booking_details.objects.all()

        booking = get_object_or_404(queryset, Slug=slug)

        return render(request, "booking/booking_details.html",
                      {"booking": booking, "booking_form": BookingForms()})

    
class Name(View):

    def get(self, request, *args, **kwargs):

        return render(request, "booking/name.html",
                      {"booking_form": BookingForms()})

    def post(self, request, *args, **kwargs):
        
        booking_form = BookingForms(request.POST)

        Phone_no = request.POST.get('Phone_Number')
        
        if booking_form.is_valid():
            booking_form.save()

        else:
            booking_form = BookingForms()

        bookings = get_object_or_404(Booking_details, Phone_Number=Phone_no)
        
        return render(request, "booking/show_booking.html",
                      {"bookings": bookings})


class ShowBooking(View):

    def get(self, request, *args, **kwargs):

        return render(request, "booking/show_booking.html")


class HomePage(View):

    def get(self, request, *args, **kwargs):

        queryset = Menu.objects.all()

        photo1 = get_object_or_404(queryset, Meal_Name="Cheese Burger")
        photo2 = get_object_or_404(queryset, Meal_Name="Double Cheese Burger")
        photo3 = get_object_or_404(
            queryset, Meal_Name="Beef Burger with mushroom")
        return render(request, "booking/homepage.html",
                      {"photo1": photo1, "photo2": photo2, "photo3": photo3})


class EditBooking(View):

    def get(self, request, booking_id, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, id=booking_id)

        if request.method == 'POST':

            form = BookingForms(request.POST, instance=book_detail)

            if form.is_valid():
                form.save()
                return redirect('booking/booking_details.html')

            form = BookingForms(instance=book_detail)
            
            return render(request, 'booking/show_booking.html', {"form": form})


class DeleteBooking(View):
        
    def delete_booking(self, request, booking_id,*args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, id=booking_id)

        book_detail.delete()

        return redirect('booking/booking_details.html')




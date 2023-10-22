from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic, View
from .models import Booking_details, Menu
from .forms import BookingForms, Pre_Booking
from random import *
import urllib.request
import urllib.error
# Create your views here.

''' Create a View for Booking_List Model '''

class BookingList(generic.ListView):

    model = Menu
    queryset = Menu.objects.all()
    template_name = 'booking/homepage.html'

# Create a View for the Menu Model 

class MenuList(generic.ListView):

    model = Menu
    queryset = Menu.objects.all()
    template_name = 'booking/menu.html'

# Create a get and post method for the Booking Details 


class BookingDetails(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Booking_details.objects.all()

        booking = get_object_or_404(queryset, Slug=slug)

        return render(request, "booking/booking_details.html",
                      {"booking": booking, "booking_form": BookingForms()})

# Create a get and post method for the Name class which get the data 
# from the booking form in the booking tab 


class Name(View):

    def get(self, request, *args, **kwargs):

        return render(request, "booking/name.html",
                      {"booking_form": BookingForms()})

    def post(self, request, *args, **kwargs):

        Phone_no = request.POST.get('Phone_Number')

        try:
            bookings_user = get_object_or_404(Booking_details, Slug=Phone_no)
            return render(request, "booking/show_booking.html",
                          {"bookings": bookings_user})

        except:
            booking_form = BookingForms(request.POST)
            if booking_form.is_valid():
                booking_form.save()
                Booking_details.objects.filter(
                    Phone_Number=Phone_no).update(Slug=Phone_no)
                bookings_user = get_object_or_404(
                    Booking_details, Slug=Phone_no)
                return render(request, "booking/show_booking.html",
                              {"bookings": bookings_user})

            else:
                booking_form = BookingForms()

# create Showbooking class to show booking after being created 


class ShowBooking(View):

    def get(self, request, *args, **kwargs):

        return render(request, "booking/show_booking.html")

# Create Homapge class View to render the images from the Menu model in the Home page 


class HomePage(View):

    def get(self, request, *args, **kwargs):

        queryset = Menu.objects.all()

        photo1 = get_object_or_404(queryset, Meal_Name="Cheese Burger")
        photo2 = get_object_or_404(queryset, Meal_Name="Double Cheese Burger")
        photo3 = get_object_or_404(
            queryset, Meal_Name="Beef Burger with mushroom")
        return render(request, "booking/homepage.html",
                      {"photo1": photo1, "photo2": photo2, "photo3": photo3})

# Create Edit view to show the edit of the Booking 


class EditBooking(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, Slug=slug)
        booking_form = BookingForms(instance=book_detail)

        return render(request, 'booking/editbooking.html', {"form": booking_form})

    def post(self, request, slug, *args, **kwargs):

        booking_ins = get_object_or_404(Booking_details, Slug=slug)

        booking_form_1 = BookingForms(request.POST, instance=booking_ins)

        if booking_form_1.is_valid():
            booking_form_1.save()

        else:
            booking_form_1 = BookingForms()

        booking = request.POST.get('Phone_Number')
        bookings = get_object_or_404(Booking_details, Phone_Number=booking)

        return render(request, "booking/show_booking.html",
                      {"bookings": bookings})

# Create delete view to show the edit of the Booking 


class DeleteBooking(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, Slug=slug)
        booking_form_2 = BookingForms(instance=book_detail)

        return render(request, 'booking/deletebooking.html', {"form": booking_form_2})

    def post(self, request, slug, *args, **kwargs):

        booking_ins = get_object_or_404(Booking_details, Slug=slug)

        booking_ins.delete()

        queryset = Menu.objects.all()

        photo1 = get_object_or_404(queryset, Meal_Name="Cheese Burger")
        photo2 = get_object_or_404(queryset, Meal_Name="Double Cheese Burger")
        photo3 = get_object_or_404(
            queryset, Meal_Name="Beef Burger with mushroom")

        return render(request, "booking/homepage.html", {"photo1": photo1,
                                                         "photo2": photo2,
                                                         "photo3": photo3})


class PreviousBooking(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'booking/previousbook.html',
                      {"form": Pre_Booking()})

    def post(self, request, *args, **kwargs):

        booking_1 = request.POST.get('Phone_Number')
        booking_pre = get_list_or_404(Booking_details, Slug=booking_1)

        return render(request, "booking/show_previous_booking.html",
                      {"bookings": booking_pre})

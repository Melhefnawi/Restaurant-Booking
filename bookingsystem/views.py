from django.shortcuts import (render, redirect,
                              get_object_or_404, get_list_or_404)
from django.views import generic, View
from .models import Booking_details, Menu
from django.contrib.auth.models import User
from .forms import BookingForms
import urllib.request
import urllib.error
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
import re


# Create a View for the Menu Model


class MenuList(generic.ListView):

    model = Menu
    queryset = Menu.objects.all()
    template_name = 'booking/menu.html'

# Create a get  method for the Booking Details class


class BookingDetails(LoginRequiredMixin, UserPassesTestMixin,View):

    
    

    def get(self, request, id, *args, **kwargs):

       
        queryset = Booking_details.objects.all()

        booking = get_object_or_404(queryset, pk=id)

        return render(request, "booking/booking_details.html",
                      {"booking": booking, "booking_form": BookingForms()})



    def test_func(self):
        
        pk = self.kwargs.get('id')
        queryset = Booking_details.objects.all()
        booking = get_object_or_404(queryset, pk=pk)
        return self.request.user == booking.User
        
       


class BookingForm(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        form = BookingForms(initial={'User': self.request.user})
        return render(request, "booking/bookingform.html",
                      {"booking_form": form})

    def post(self, request, *args, **kwargs):

        Phone_no = request.POST.get('Phone_Number')
        People_No = request.POST.get('People_No')

        if Phone_no.startswith("+"):
            messages.success(request, 'Please enter valid numer without sign')
            return render(request, "booking/bookingform.html",
                          {"booking_form": BookingForms(initial={'User': self.request.user})})
        elif Phone_no.startswith("-"):
            messages.success(request, 'Please enter valid numer without sign')
            return render(request, "booking/bookingform.html",
                          {"booking_form": BookingForms(initial={'User': self.request.user})})
        elif  People_No.startswith("-"):
            messages.success(request, 'Please enter valid numer without sign')
            return render(request, "booking/bookingform.html",
                          {"booking_form": BookingForms(initial={'User': self.request.user})})
        else:

            booking_form = BookingForms(request.POST, initial={'User': self.request.user})
            if booking_form.is_valid():
                booking_form.save()
                messages.success(request, 'Form submission successful')
                return redirect('homepage')

# create Showbooking class to show booking after being created


class ShowAllBooking(LoginRequiredMixin, UserPassesTestMixin,View):

    def get(self, request, *args, **kwargs):

        all_booking = Booking_details.objects.all()

        return render(request, "booking/show_all_bookings.html",
                      {"bookings": all_booking})

    def test_func(self):

        return self.request.user.is_superuser

class ShowBooking(LoginRequiredMixin, UserPassesTestMixin,View):

    def get(self, request, *args, **kwargs):

        return render(request, "booking/show_booking.html")

    def test_func(self):

        pk = self.kwargs.get('id')
        queryset = Booking_details.objects.all()
        booking = get_object_or_404(queryset, pk=pk)
        return self.request.user == booking.User

# Create Homapge class View to render the images from the Menu model in
# the Home page


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


class EditBooking(LoginRequiredMixin, UserPassesTestMixin,View):

    def get(self, request, id, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, pk=id)
        booking_form = BookingForms(instance=book_detail)
        return render(request, 'booking/editbooking.html',
                      {"form": booking_form})

    def post(self, request, id, *args, **kwargs):

        booking_ins = get_object_or_404(Booking_details, pk=id)
        booking_form_1 = BookingForms(request.POST, instance=booking_ins)
        if booking_form_1.is_valid():
            booking_form_1.save()
            messages.success(request, "Profile details updated.")
        else:
            booking_form_1 = BookingForms()

        bookings = Booking_details.objects.filter(pk=id)

        return render(request, "booking/show_booking.html",
                      {"bookings": bookings})
    
    def test_func(self):

        pk = self.kwargs.get('id')
        queryset = Booking_details.objects.all()
        booking = get_object_or_404(queryset, pk=pk)
        return self.request.user == booking.User

# Create delete view with get and post to delete the Booking


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin,View):

    def get(self, request, id, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, pk=id)
        booking_form_2 = BookingForms(instance=book_detail)

        return render(request, 'booking/deletebooking.html',
                      {"form": booking_form_2})

    def post(self, request, id, *args, **kwargs):

        booking_ins = get_object_or_404(Booking_details, pk=id)

        booking_ins.delete()
        messages.error(request, "Booking deleted.")

        queryset = Menu.objects.all()
        photo1 = get_object_or_404(queryset, Meal_Name="Cheese Burger")
        photo2 = get_object_or_404(queryset, Meal_Name="Double Cheese Burger")
        photo3 = get_object_or_404(
            queryset, Meal_Name="Beef Burger with mushroom")

        return render(request, "booking/homepage.html", {"photo1": photo1,
                                                         "photo2": photo2,
                                                         "photo3": photo3})

    def test_func(self):

      
        pk = self.kwargs.get('id')
        queryset = Booking_details.objects.all()
        booking = get_object_or_404(queryset, pk=pk)
        return self.request.user == booking.User


class ApproveBooking(LoginRequiredMixin, UserPassesTestMixin,View):

    def get(self, request, id, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, pk=id)
        booking_form_2 = BookingForms(instance=book_detail)

        return render(request, 'booking/approvebooking.html',
                      {"form": booking_form_2})

    def post(self, request, id, *args, **kwargs):

        Booking_details.objects.filter(pk=id).update(approved=True)
        messages.success(request, "The booking is approved")

        queryset = Menu.objects.all()
        # getting images from Menu model
        photo1 = get_object_or_404(queryset, Meal_Name="Cheese Burger")
        photo2 = get_object_or_404(queryset, Meal_Name="Double Cheese Burger")
        photo3 = get_object_or_404(
            queryset, Meal_Name="Beef Burger with mushroom")

        return render(request, "booking/homepage.html", {"photo1": photo1,
                                                         "photo2": photo2,
                                                         "photo3": photo3})
    def test_func(self):

        return self.request.user.is_superuser

class ShowPreviousBooking(LoginRequiredMixin, UserPassesTestMixin,View):

    def get(self, request, *args, **kwargs):

        bookings = Booking_details.objects.filter(User=self.request.user)

        return render(request, "booking/show_booking.html",
                      {"bookings": bookings})

    def test_func(self):

        
        return self.request.user.is_authenticated
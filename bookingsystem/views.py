from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic, View
from .models import Booking_details, Menu
from django.contrib.auth.models import User
from .forms import BookingForms
import urllib.request
import urllib.error
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import re


# Create a View for the Menu Model


class MenuList(generic.ListView):

    model = Menu
    queryset = Menu.objects.all()
    template_name = 'booking/menu.html'

# Create a get  method for the Booking Details class 






class BookingDetails(View):

    def get(self, request, id, *args, **kwargs):

        queryset = Booking_details.objects.all()

        booking = get_object_or_404(queryset, pk=id)

        return render(request, "booking/booking_details.html",
                      {"booking": booking, "booking_form": BookingForms()})

    
# Create a get and post method for the Booking_form class which get the data
# from the booking form in the booking tab and save it to the Database 


class BookingForm(LoginRequiredMixin, View):

    

    def get(self, request, *args, **kwargs):
        
        form = BookingForms(initial={'User': request.user})
        
        return render(request, "booking/bookingform.html",
                      {"booking_form": form})

    def post(self, request, *args, **kwargs):

        Phone_no = request.POST.get('Phone_Number')

        if  Phone_no.startswith("+"):
            messages.success(request, 'Please enter a valid data Phone numer without any sign ')
            return render(request, "booking/bookingform.html", {"booking_form": BookingForms()}) 
                      
        #elif Booking_details.objects.filter(Phone_Number=Phone_no).exists():
           # messages.info(request, "Previous Booking")
           # booking = request.POST.get('Phone_Number')
            # bookings = get_object_or_404(Booking_details, Slug=booking)
           # bookings = Booking_details.objects.filter(Phone_Number=booking)
            #return render(request, "booking/show_all_prev_bookings.html",
                      #  {"bookings": bookings})
        else:
                    
            booking_form = BookingForms(request.POST)
            if booking_form.is_valid():
                booking_form.save()
                messages.success(request, 'Form submission successful')
                booking = request.POST.get('Phone_Number')
                bookings = Booking_details.objects.filter(Phone_Number=booking)
                return render(request, "booking/show_booking.html",
                             {"bookings": bookings})

# create Showbooking class to show booking after being created

class ShowAllBooking(View):

    def get(self, request, *args, **kwargs):

        all_booking = Booking_details.objects.all()

        return render(request, "booking/show_all_bookings.html",
                      {"bookings": all_booking})

       

class ShowBooking(View):

    def get(self, request, *args, **kwargs):

        return render(request, "booking/show_booking.html")

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


class EditBooking(View):

    def get(self, request, id, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, pk=id)
        booking_form = BookingForms(instance=book_detail)
        return render(request, 'booking/editbooking.html', {"form": booking_form})

    def post(self, request, id, *args, **kwargs):

        booking_ins = get_object_or_404(Booking_details, pk=id)
        booking_form_1 = BookingForms(request.POST, instance=booking_ins)
        if booking_form_1.is_valid():
            booking_form_1.save()
            messages.success(request, "Profile details updated.")
        else:
            booking_form_1 = BookingForms()

        #booking = request.POST.get('Phone_Number')
        bookings = Booking_details.objects.filter(pk=id)

        return render(request, "booking/show_booking.html",
                      {"bookings": bookings})

# Create delete view with get and post to delete the Booking


class DeleteBooking(View):

    def get(self, request, id, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, pk=id)
        booking_form_2 = BookingForms(instance=book_detail)

        return render(request, 'booking/deletebooking.html', {"form": booking_form_2})

    def post(self, request, id, *args, **kwargs):

        booking_ins = get_object_or_404(Booking_details, pk=id)

        booking_ins.delete()
        messages.error(request, "Booking deleted.")

        queryset = Menu.objects.all()
        # getting images from Menu model to render them in the homepage template
        photo1 = get_object_or_404(queryset, Meal_Name="Cheese Burger")
        photo2 = get_object_or_404(queryset, Meal_Name="Double Cheese Burger")
        photo3 = get_object_or_404(
            queryset, Meal_Name="Beef Burger with mushroom")

        return render(request, "booking/homepage.html", {"photo1": photo1,
                                                         "photo2": photo2,
                                                         "photo3": photo3})


class ApproveBooking(View):

    def get(self, request, id, *args, **kwargs):

        queryset = Booking_details.objects.all()
        book_detail = get_object_or_404(queryset, pk=id)
        booking_form_2 = BookingForms(instance=book_detail)

        return render(request, 'booking/approvebooking.html', {"form": booking_form_2})

    def post(self, request, id, *args, **kwargs):

        Booking_details.objects.filter(pk=id).update(approved=True)
        
        messages.success(request, "The booking is approved")

        queryset = Menu.objects.all()
        # getting images from Menu model to render them in the homepage template
        photo1 = get_object_or_404(queryset, Meal_Name="Cheese Burger")
        photo2 = get_object_or_404(queryset, Meal_Name="Double Cheese Burger")
        photo3 = get_object_or_404(
            queryset, Meal_Name="Beef Burger with mushroom")

        return render(request, "booking/homepage.html", {"photo1": photo1,
                                                         "photo2": photo2,
                                                         "photo3": photo3})                  


class ShowPreviousBooking(View):


    def get(self, request, *args, **kwargs):

        bookings = Booking_details.objects.filter(User=self.request.user)

        
        return render(request, "booking/show_booking.html",
                             {"bookings": bookings})

        


    
    
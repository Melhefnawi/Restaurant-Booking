from django.contrib import admin
from .models import Booking_details, Client, Menu
# Register your models here.

@admin.register (Booking_details)
class BookingAdmin(admin.ModelAdmin):
    
@admin.register (Client)
@admin.register (Menu)



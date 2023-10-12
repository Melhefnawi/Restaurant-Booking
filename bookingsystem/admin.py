from django.contrib import admin
from .models import Booking_details, Client, Menu
# Register your models here.


@admin.register(Booking_details)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Date', 'Time',
                    'People_No', 'approved')
    search_fields = ['First_Name', 'Date']
    list_filter = ('First_Name', 'Last_Name')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name')
    search_fields = ['First_Name']
    list_filter = ('First_Name', 'Last_Name')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ['Feature_image']

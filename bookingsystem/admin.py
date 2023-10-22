from django.contrib import admin
from .models import Booking_details, Menu
# Register your models here.

# Register the Booking_Details Model to the admin panel


@admin.register(Booking_details)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Slug', 'Date', 'Time',
                    'People_No', 'approved')
    search_fields = ['First_Name', 'Date']
    list_filter = ('First_Name', 'Last_Name')
    prepopulated_fields = {'Slug': ('Email',)}

    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)


# Register the Menu Model to admin Panel

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('Featured_image', 'Meal_Name', 'Meal_des')
    search_fields = ['Feature_image', 'Meal_Name']

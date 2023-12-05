from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('booking', views.BookingForm.as_view(), name='booking'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('<slug:slug>', views.BookingDetails.as_view(),
         name='Booking_details'),
    path('booking/show_booking', views.ShowBooking.as_view(),
         name='Show_Booking'),
    
    path('booking/editbooking/<slug:slug>', views.EditBooking.as_view(), name='edit_booking'),
    path('booking/deletebooking/<slug:slug>', views.DeleteBooking.as_view(), name='delete_booking'),
    path('booking/show_all_bookings/', views.ShowAllBooking.as_view(), name='showallbookings'),
    
]

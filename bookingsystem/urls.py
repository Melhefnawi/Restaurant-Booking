from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('booking', views.Name.as_view(), name='booking'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('<str:First_Name>', views.BookingDetails.as_view(),
         name='Booking_details'),
    path('booking/show_booking', views.ShowBooking.as_view(), name='Show_Booking'),
    
]

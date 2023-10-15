from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('booking', views.Name.as_view(), name='booking'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('<slug:slug>', views.BookingDetails.as_view(),
         name='Booking_details'),
    path('booking/show_booking', views.ShowBooking.as_view(),
         name='Show_Booking'),
    path('booking/homepage', views.HomePage.as_view(), name='homepage'),
    path('booking/homepage', views.EditBooking.as_view(), name='homepage'),
    path('booking/homepage', views.DeleteBooking.as_view(), name='homepage'),

]

from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('<str:First_Name>', views.BookingDetails.as_view(),
         name='Booking_details')
]

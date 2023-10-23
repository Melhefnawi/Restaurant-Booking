from django.test import TestCase

from .models import Booking_details

# Create your tests here.


class TestViews(TestCase):

    def test_menulist(self):
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/menu.html')

    def test_name(self):
        response = self.client.get('/booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking/name.html")

    def test_showbooking(self):
        booking_test = Booking_details.objects.create(
            First_Name='Mo', Last_Name='Mo', Slug=4)
        response = self.client.get(
            f'/booking/show_booking/{booking_test.Slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking/show_booking.html")

    def test_bookingdetails(self):
        booking_test = Booking_details.objects.create(
            First_Name='Mo', Last_Name='Mo', Slug=4)
        response = self.client.get(f'/{booking_test.Slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_details.html')

    def test_homepage(self):
        response = self.client.get()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/booking/homepage.html')

    def test_editbooking(self):
        booking_test = Booking_details.objects.create(
            First_Name='Mo', Last_Name='Mo', Slug=4)
        response = self.client.get(f'/booking/editbooking/{booking_test.Slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/editbooking.html')

    def test_deletebooking(self):
        booking_test = Booking_details.objects.create(
            First_Name='Mo', Last_Name='Mo', Slug=4)
        response = self.client.get(
            f'/booking/deletebooking/{booking_test.Slug}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(booking_test.approved, 0)
        self.assertEqual(booking_test.Time, null)
        self.assertTemplateUsed(response, 'booking/deletebooking.html')
        

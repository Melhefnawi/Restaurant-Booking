from django.test import TestCase

from .models import Booking_details, Menu

# Create your tests here.


class TestModels(TestCase):

    def test_done_defaults_to_false(self):

        booking_test = Booking_details.objects.create(First_Name='MO', Last_Name='MO',
                                                      Date='2023-3-4', Time='4:00',
                                                      Email='mmm@yyy.com', Phone_Number=98888, Slug='998877', People_No=6)
        booking_test_2 = Menu.objects.create(
            Featured_image='placeholder', Meal_Name='beef burger', Meal_des='beef burger')

        self.assertFalse(booking_test.approved)

from django.test import TestCase

from .forms import BookingForms

# Create your tests here.


class TestBookingForms(TestCase):

    def test_first_name_is_required(self):

        form = BookingForms({'First_Name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('First_Name', form.errors.keys())
        self.assertEqual(form.errors['First_Name'][0], 'This field is required.')

    def test_last_name_is_required(self):

        form = BookingForms({'Last_Name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Last_Name', form.errors.keys())
        self.assertEqual(form.errors['Last_Name'][0], 'This field is required.')

    def test_date_is_required(self):

        form = BookingForms({'Date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Date', form.errors.keys())
        self.assertEqual(form.errors['Date'][0], 'This field is required.')     
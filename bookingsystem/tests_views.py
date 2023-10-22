from django.test import TestCase

from .forms import BookingForms

# Create your tests here.


class TestViews(TestCase):

    def test_first_name_is_required(self):

        form = BookingForms({'First_Name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('First_Name', form.errors.keys())
        self.assertEqual(form.errors['First_Name']
                         [0], 'This field is required.')

    def test_last_name_is_required(self):

        form = BookingForms({'Last_Name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Last_Name', form.errors.keys())
        self.assertEqual(form.errors['Last_Name']
                         [0], 'This field is required.')

    def test_date_is_required(self):

        form = BookingForms({'Date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Date', form.errors.keys())
        self.assertEqual(form.errors['Date'][0], 'This field is required.')

    def test_time_is_required(self):

        form = BookingForms({'Time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Time', form.errors.keys())
        self.assertEqual(form.errors['Time'][0], 'This field is required.')

    def test_phone_number_is_required(self):

        form = BookingForms({'Phone_Number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Phone_Number', form.errors.keys())
        self.assertEqual(form.errors['Phone_Number']
                         [0], 'This field is required.')

    def test_phone_number_is_required(self):

        form = BookingForms({'Phone_Number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Phone_Number', form.errors.keys())
        self.assertEqual(form.errors['Phone_Number']
                         [0], 'This field is required.')

    def test_people_no_is_required(self):

        form = BookingForms({'People_No': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('People_No', form.errors.keys())
        self.assertEqual(form.errors['People_No']
                         [0], 'This field is required.')

    def test_email_is_required(self):

        form = BookingForms({'Email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Email', form.errors.keys())
        self.assertEqual(form.errors['Email']
                         [0], 'This field is required.')


    def test_fields_are_explicite_in_form_metaclass(self):

        form = BookingForms()
        self.assertEqual(form.Meta.fields, ('First_Name', 'Last_Name', 'Date',
                                            'Time', 'Phone_Number', 'People_No', 'Email'))

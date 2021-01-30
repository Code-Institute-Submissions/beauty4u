from django.test import TestCase
from .models import Bookings
import unittest


class testBookingModel(TestCase):

    def test_booking_has_id(self):

        """
        Test to check if a booking id is always created when a booking is made
        """

        booking = Bookings.objects.create(customer_name="David")
        booking.save()
        self.assertIsNotNone(booking.booking_id)

    @unittest.expectedFailure
    def test_booking_id_length(self):

        """
        Test booking id generated correctly  - test expected to fail

        """

        self.assertLessEqual(len(self.booking.booking_id), 20)
        self.assertEqual(len(self.booking.booking_id), 32)

    def test_redirect_no_login(self):

        """
        Test a redirect due to no login on the booking page

        """

        response = self.client.get('/booking')
        self.assertEqual(response.status_code, 301)

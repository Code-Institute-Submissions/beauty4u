from django.test import TestCase
from .models import Bookings
from django.conf import settings
import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from allauth.utils import get_user_model, get_username_max_length
from django.urls import reverse
from django.contrib.auth import views

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

        self.assertLessEqual(len(booking.booking_id), 20)
        self.assertEqual(len(booking.booking_id), 32)
       
    def test_redirect_no_login(self):


        """
        Test a redirect due to no login on the booking page 

        """

        response = self.client.get('/booking')
        self.assertEqual(response.status_code, 301)

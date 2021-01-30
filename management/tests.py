from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .views import update_booking_status, Bookings, save_data
from .models import Sitesettings
import json


class testBookingModel(TestCase):

    def setUp(self):

        """
        Create super user for testing

        """
        # Set Up Super User Access
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='david', email='david@test.com', password='david')
        self.user.is_superuser = True
        # Set up new booking
        self.booking = Bookings.objects.create(customer_name="David",
                                               username="david")
        self.booking_id = self.booking.booking_id
        self.booking.save()
        # Set up site setting to mock click & collect setting and set to false
        self.setting = Sitesettings.objects.create(name="Click & Collect")
        self.setting.status = False
        self.setting.save()

    def test_confirm_booking(self):

        """

        A test that checks when a booking id is posted
        to update_booking_status, that the confirmed status
        of the booking is changed and the correct
        booking id is returned

        """

        request = self.factory.post(reverse('update_booking_status'),
                                    {'customer_name': 'David',
                                     'confirmBooking': True,
                                     'bookingDate': '01/06/2021',
                                     'time': '09:00',
                                     'bookingId': self.booking_id})
        request.user = self.user
        response = update_booking_status(request)
        self.assertEqual(
            json.loads(response.content)['booking_id'], self.booking_id)
        self.assertEqual(
            json.loads(response.content)['confirmedStatus'], 'True')

    def test_shipping_setting(self):

        """

        A test that checks when the toggle click & collect option is
        toggled to no, that the setting is set to no

        """

        request = self.factory.post(reverse('save_data'), {
                                            'settingName': 'Click & Collect',
                                            'settingStatus': 'True'})
        request.user = self.user
        response = save_data(request)
        self.assertEqual(json.loads(response.content)['setting'], 'True')
        self.assertEqual(response.status_code, 200)

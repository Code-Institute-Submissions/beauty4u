from django.test import TestCase
from .models import Order
import unittest


class testOrderModel(TestCase):
    def test_order_has_order_number(self):

        """

        Test to check if an order number is always created when an order is saved 
        
        """

        order = Order.objects.create(full_name="David")
        order.save()
        self.assertIsNotNone(order.order_number)

        

    @unittest.expectedFailure
    def test_order_number_length(self):

        """
        Test order number generated correctly  - test expected to fail

        """

        self.assertLessEqual(len(order.order_number), 20)
        self.assertEqual(len(order.order_number), 32)
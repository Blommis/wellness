from django.test import TestCase
from django.contrib import admin
from checkout.admin import OrderAdmin, OrderLineItemAdminInline
from checkout.models import Order


class CheckoutAdminTests(TestCase):
    def test_order_model_registered(self):
        """Ensure the Order model is registered in admin with OrderAdmin"""
        self.assertIn(Order, admin.site._registry)
        self.assertIsInstance(admin.site._registry[Order], OrderAdmin)

    def test_order_admin_has_inline(self):
        """Ensure the OrderAdmin includes OrderLineItem inline"""
        self.assertIn(OrderLineItemAdminInline, OrderAdmin.inlines)

    def test_order_admin_readonly_fields(self):
        """Check readonly fields in OrderAdmin"""
        readonly_fields = (
            'order_number', 'date', 'delivery_cost',
            'order_total', 'grand_total'
        )
        for field in readonly_fields:
            self.assertIn(field, OrderAdmin.readonly_fields)

    def test_order_admin_fields(self):
        """Check that all expected fields are in OrderAdmin.fields"""
        expected_fields = (
            'order_number', 'user_profile', 'date', 'full_name',
            'email', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county', 'delivery_cost', 'order_total', 'grand_total',
        )
        for field in expected_fields:
            self.assertIn(field, OrderAdmin.fields)

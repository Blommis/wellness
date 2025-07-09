from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Order, OrderLineItem
from products.models import Supplement, MealPlan
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
import json
import time
import stripe
from django.conf import settings

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        print("SENDING EMAIL TO:", order.email)
        
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )
        
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        """ This function is taken inspiration from Boutinque ado """
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.get('bag', '{}')
        bag_data = json.loads(bag)
        save_info = intent.metadata.get('save_info', False)
        username = intent.metadata.get('username', 'AnonymousUser')

        """ Retrieve charge details for billing info """
        charge = stripe.Charge.retrieve(intent.latest_charge)

        email = intent.metadata.get('email', 'noemail@placeholder.com')
        full_name = intent.metadata.get('full_name', '')
        phone = intent.metadata.get('phone', '')
        country = intent.metadata.get('country', '')
        postcode = intent.metadata.get('postcode', '')
        city = intent.metadata.get('town_or_city', '')
        line1 = intent.metadata.get('street_address1', '')
        line2 = intent.metadata.get('street_address2', '')
        state = intent.metadata.get('county', '')
        
        """ Clean empty strings from shipping address """
    
        grand_total = round(charge.amount / 100, 2)

        profile = None
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info and profile:
                    profile.default_phone_number = phone
                    profile.default_country = country
                    profile.default_postcode = postcode
                    profile.default_town_or_city = city
                    profile.default_street_address1 = line1
                    profile.default_street_address2 = line2
                    profile.default_county = state
                    profile.save()
            except UserProfile.DoesNotExist:
                profile = None
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                 full_name=full_name,
                 phone_number=phone,
                 country=country,
                 postcode=postcode,
                 town_or_city=city,
                 street_address1=line1,
                 street_address2=line2,
                 county=state,
                 grand_total=grand_total,
                 original_bag=bag,
                 stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=full_name,
                    user_profile=profile,
                    email=email,
                    phone_number=phone,
                    country=country,
                    postcode=postcode,
                    town_or_city=city,
                    street_address1=line1,
                    street_address2=line2,
                    county=state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                for item_key, item_data in bag_data.items():
                    product_type, object_id = item_key.split('_')
                    object_id = int(object_id)
                    quantity = item_data.get('quantity', 1)

                    if product_type == 'supplement':
                        model = Supplement
                    elif product_type == 'mealplan':
                        model = MealPlan
                    else:
                        continue

                    product = model.objects.get(id=object_id)
                    content_type = ContentType.objects.get_for_model(model)

                    OrderLineItem.objects.create(
                        order=order,
                        content_type=content_type,
                        object_id=product.id,
                        quantity=quantity,
                    )

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {str(e)}',
                    status=500
                )
            
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)


    
    def handle_payment_intent_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content='PaymentIntent failed',
            status=200
        )

    

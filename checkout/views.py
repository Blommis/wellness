from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from bag.context_processors import bag_contents
from django.conf import settings
import stripe
from .models import Order
import json
import time

# Create your views here.


def checkout(request):
    """
    handles the order process. It validates the bag and form data,
    saves the order and related items, and sets up Stripe payment.
    If the user is authenticated, their profile data pre-fills the form.

    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "Unfortunately, your bag is empty.")
        return redirect(reverse('home:index'))

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            pid = request.POST.get('client_secret').split('_secret')[0]
            request.session['save_info'] = 'save-info' in request.POST

            return redirect('checkout_success', stripe_pid=pid)
        else:
            messages.error(
                request,
                "There was an error with your form. Please check your details."
            )
            return redirect('checkout')
    else:
        bag_data = bag_contents(request)
        total = bag_data['grand_total']
        stripe_total = round(total * 100)

        initial_data = {}

        if request.user.is_authenticated:
            try:
                profile = request.user.userprofile
                initial_data = {
                    'email': request.user.email,
                    'full_name': request.user.get_full_name(),
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                }
            except Exception:
                pass
        order_form = OrderForm(initial=initial_data)

        metadata = {
            'bag': json.dumps(bag),
            'username': (
                request.user.username
                if request.user.is_authenticated
                else 'AnonymousUser'
            ),
            'save_info': False,
        }

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata=metadata
        )

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'bag_items': bag_data['bag_items'],
            'order_total': bag_data['total'],
            'delivery_cost': bag_data['delivery'],
            'grand_total': bag_data['grand_total'],
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)


def checkout_success(request, stripe_pid):
    """
    retrieves the order, clears the bag from the session,
    shows a success message, and renders the confirmation page.
    """
    order = None
    attempt = 1

    while attempt <= 5:
        order = Order.objects.filter(stripe_pid=stripe_pid).first()
        if order:
            break
        attempt += 1
        time.sleep(1)

    if not order:
        messages.error(request, "Your order could not be found.")
        return redirect('home:index')

    # Empty bag
    if 'bag' in request.session:
        del request.session['bag']

    messages.success(
        request,
        f"Order {order.order_number} confirmed! "
        f"A confirmation email will be sent to {order.email}."
    )

    return render(request, 'checkout/checkout_success.html', {'order': order})

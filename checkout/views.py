from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from bag.context_processors import bag_contents
from django.conf import settings
import stripe
# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Unfortunately, your bag is empty.")
        return redirect(reverse('home'))

    bag_data = bag_contents(request)
    total = bag_data['grand_total']
    stripe_total = round(total * 100)
    
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'bag_items': bag_data['bag_items'],
        'order_total': bag_data['total'],
        'delivery_cost': bag_data['delivery'],
        'grand_total': bag_data['grand_total'],
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

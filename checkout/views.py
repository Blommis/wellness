from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from bag.context_processors import bag_contents
from django.conf import settings
import stripe
from .models import Order, OrderLineItem
from products.models import Supplement, MealPlan
from django.contrib.contenttypes.models import ContentType
from profiles.models import UserProfile
import json

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "Unfortunately, your bag is empty.")
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form_data = request.POST
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)

            if request.user.is_authenticated:
                order.user_profile = request.user.userprofile
                
            order.save()

            for item_key, item_data in bag.items():
                try:
                    product_type, object_id = item_key.split("_")  # 'supplement' or 'mealplan'
                    object_id = int(object_id)
                except ValueError:
                    continue

                quantity = item_data.get('quantity', 1)

                if product_type == 'supplement':
                    model = Supplement
                elif product_type == 'mealplan':
                    model = MealPlan
                else:
                    continue  

                product = get_object_or_404(model, pk=object_id)
                content_type = ContentType.objects.get_for_model(model)

                lineitem = OrderLineItem(
                    order=order,
                    content_type=content_type,
                    object_id=product.id,
                    quantity=quantity,
                )
                lineitem.save()
                
            return redirect('checkout_success', order_number=order.order_number)
        else: 
            messages.error(request, "There was an error with your form. Please check your details.")
            return redirect('checkout')
    
    else: 
        bag_data = bag_contents(request)
        total = bag_data['grand_total']
        stripe_total = round(total * 100)
        
        if request.user.is_authenticated:

            try:
                profile = request.user.userprofile
                initial_data = {
                    'email': request.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                }
                order_form = OrderForm(initial=initial_data)

            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        metadata={
            'bag': json.dumps(bag),
            'username': request.user.username if request.user.is_authenticated else 'AnonymousUser',
            'save_info': request.POST.get('save_info', False),
            'email': request.POST.get('email'),
            'full_name': request.POST.get('full_name'),
            'phone': request.POST.get('phone_number'),
            'country': request.POST.get('country'),
            'postcode': request.POST.get('postcode'),
            'town_or_city': request.POST.get('town_or_city'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'county': request.POST.get('county'),
        }
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


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # Empty bag
    if 'bag' in request.session:
        del request.session['bag']

    messages.success(request, f"Order {order_number} confirmed! A confirmation email will be sent to {order.email}.")

    return render(request, 'checkout/checkout_success.html', {'order': order})




    

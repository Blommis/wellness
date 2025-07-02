from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from bag.context_processors import bag_contents
from django.conf import settings
import stripe
from .models import Order, OrderLineItem
from products.models import Supplement, MealPlan
from django.contrib.contenttypes.models import ContentType

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
            order = order_form.save()
            order.order_total = 0
            order.delivery_cost = 0
            order.grand_total = 0
            order.save()

            total = 0

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

                OrderLineItem.objects.create(
                    order=order,
                    content_type=content_type,
                    object_id=product.id,
                    quantity=quantity,
                )
                total += product.price * quantity

            order.order_total = total
            order.grand_total = total
            order.save()

            return redirect('checkout_success', order_number=order.order_number)
        else: 
            messages.error(request, "There was an error with your form. Please check your details.")
            return redirect('checkout')
    
    else: 
        bag_data = bag_contents(request)
        total = bag_data['grand_total']
        stripe_total = round(total * 100)
    
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




    

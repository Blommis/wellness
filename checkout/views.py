from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from bag.context_processors import bag_contents

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Unfortunately, your bag is empty.")
        return redirect(reverse('home'))

    order_form = OrderForm()

    bag_data = bag_contents(request)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'bag_items': bag_data['bag_items'],
        'order_total': bag_data['total'],
        'delivery_cost': bag_data['delivery'],
        'grand_total': bag_data['grand_total'],
    }

    return render(request, template, context)

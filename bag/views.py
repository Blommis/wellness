from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Supplement, MealPlan
# Create your views here.


def view_bag(request):
    """ A view to display the shopping bag contents """
    bag = request.session.get('bag', {})
    bag_items = []
    total_price = 0

    for key, item_data in bag.items():
        product_type, product_id = key.split('_')
        product_id = int(product_id)

        if product_type == 'supplement':
            product = get_object_or_404(Supplement, pk=product_id)
        elif product_type == 'mealplan':
            product = get_object_or_404(MealPlan, pk=product_id)
        else:
            continue

        quantity = item_data['quantity']
        subtotal = product.price * quantity
        total_price += subtotal

        bag_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'type': product_type,
            'key': key,
            'subtotal': subtotal,
        })

    context = {
        'bag_items': bag_items,
        'total_price': total_price,
    }
    return render(request, 'bag/bag.html', context)


def add_to_bag(request):
    """add products to shopping cart"""

    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product_type = request.POST.get('product_type')
        redirect_url = request.POST.get('redirect_url', 'view_bag')
        quantity = int(request.POST.get('quantity', 1))

        if not product_id or not product_type:
            return redirect(redirect_url)

        key = f"{product_type}_{product_id}"
        bag = request.session.get('bag', {})

        # supplement, quanity, user can user more than 1:
        if product_type == 'supplement':
            if key in bag:
                bag[key]['quantity'] += quantity
            else:
                bag[key] = {'type': product_type, 'quantity': quantity}

        # user can only pick one for each plan for each order
        elif product_type == 'mealplan':
            bag[key] = {'type': product_type, 'quantity': 1}

        request.session['bag'] = bag
        return redirect(redirect_url)

    return redirect('view_bag')


def remove_from_bag(request, item_key):
    """Remove item from shopping bag"""
    bag = request.session.get('bag', {})

    if item_key in bag:
        del bag[item_key]
        request.session['bag'] = bag
        messages.success(
            request,
            'Item removed from your bag.', extra_tags='bag')
    else:
        messages.error(
            request, 'Item not found in your bag.', extra_tags='bag')

    return redirect('view_bag')

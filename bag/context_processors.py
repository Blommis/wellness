from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Supplement, MealPlan


def cart_items_count(request):
    bag = request.session.get('bag', {})
    total_quantity = sum(item['quantity'] for item in bag.values())

    return {
        'cart_items': total_quantity
    }


def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    delivery = Decimal('7.90')
    bag = request.session.get('bag', {})

    for key, item_data in bag.items():
        product_type, product_id = key.split('_')
        product_id = int(product_id)

        if product_type == 'supplement':
            product = get_object_or_404(Supplement, pk=product_id)
        elif product_type == 'mealplan':
            product = get_object_or_404(MealPlan, pk=product_id)
        else:
            continue

        quantity = item_data.get('quantity', 1)
        subtotal = product.price * quantity
        total += subtotal
        product_count += quantity

        bag_items.append({
            'key': key,
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
        'product_count': product_count,
    }

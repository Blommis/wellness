def cart_items_count(request):
    bag = request.session.get('bag', {})
    total_quantity = sum(item['quantity'] for item in bag.values())

    return {
        'cart_items': total_quantity
    }
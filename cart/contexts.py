from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from gardensets.models import Gardenset

def cart_contents(request):

    cart_items = []
    total = 0
    gardenset_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        gardenset = get_object_or_404(Gardenset, pk=item_id)
        total += item_data * gardenset.price
        gardenset_count += item_data
        cart_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'gardenset': gardenset,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'gardenset_count': gardenset_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
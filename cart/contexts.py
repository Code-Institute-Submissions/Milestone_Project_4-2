from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from posters.models import Poster

def cart_contents(request):

    cart_items = []
    total = 0
    poster_count = 0
    savings_total = 0

    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        subtotal = 0
        poster = get_object_or_404(Poster, pk=item_id)
        if poster.disc_price:
            if poster.disc_price != 0:
                subtotal = quantity * poster.disc_price
                total += subtotal
                savings_total += (poster.price - poster.disc_price) * quantity
            else:
                subtotal = quantity * poster.price
                total += subtotal
        else:
            subtotal = quantity * poster.price
            total += subtotal
        poster_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'poster': poster,
            'subtotal': subtotal,
        })

    if total < settings.FREE_SHIP_MIN:
        shipping = total * Decimal(settings.SHIP_PERCENT / 100)
        free_ship_remain = settings.FREE_SHIP_MIN - total
    else:
        shipping = 0
        free_ship_remain = 0

    grand_total = shipping + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'poster_count': poster_count,
        'shipping': shipping,
        'free_ship_remain': free_ship_remain,
        'free_ship_min': settings.FREE_SHIP_MIN,
        'savings_total': savings_total,
        'grand_total': grand_total,
        'savings_total': savings_total,
    }

    return context
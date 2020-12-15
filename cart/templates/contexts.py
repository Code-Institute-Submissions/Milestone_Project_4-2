from decimal import Decimal
from posters.models import Poster
from django.shortcuts import get_object_or_404
from django.conf import settings

def cart_contents(request):

    c_items = []
    total = 0
    save_total = 0
    pos_amount = 0

    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        subtotal = 0
        poster = get_object_or_404(Poster, pk=item_id)
        if poster.disc_price:
            if poster.disc_price != 0:
                subtotal = quantity * poster.disc_price
                total += subtotal
                save_total += (poster.price - poster.disc_price) * quantity
            else:
                subtotal = quantity * poster.price
                total += subtotal
        else:
            subtotal = quantity * poster.price
            total += subtotal
        pos_amount += quantity
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

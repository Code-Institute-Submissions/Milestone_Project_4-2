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

    for item_id, stock in cart.items():
        subtot = 0
        poster = get_object_or_404(Poster, pk=item_id)
        if poster.disc_price:
            if poster.disc_price != 0:
                subtot = stock * poster.disc_price
                total += subtot
                save_total += (poster.price - poster.disc_price) * stock
            else:
                subtot = stock * poster.price
                total += subtot
        else:
            subtot = stock * poster.price
            total += subtot
        pos_amount += stock
        c_items.append({
            'item_id': item_id,
            'subtot': subtot,
            'stock': stock,
            'poster': poster,
        })

    if total < settings.FREE_SHIP_MIN:
        shipping = total * Decimal(settings.SHIP_PERCENT / 100)
        free_ship_remain = settings.FREE_SHIP_MIN - total
    else:
        shipping = 0
        free_ship_remain = 0

    final_total = shipping + total

    context = {
        'total': total,
        'cart_items': c_items,
        'poster_amount': pos_amount,
        'shipping': shipping,
        'free_ship_remain': free_ship_remain,
        'free_ship_min': settings.FREE_SHIP_MIN,
        'savings_total': save_total,
        'final_total': final_total,
    }

    return context
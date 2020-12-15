from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from posters.models import Poster


def view_cart(request):

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):

    poster = get_object_or_404(Poster, pk=item_id)
    stock = int(request.POST.get('stock'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += stock
        messages.success(request,
                             (f'Updated {poster.name} '
                              f'stock to {cart[item_id]}'))
    else:
        cart[item_id] = stock
        messages.success(request, f'Added {poster.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
    
def adjust_cart(request, item_id):

    poster = get_object_or_404(Poster, pk=item_id)
    stock = int(request.POST.get('stock'))
    cart = request.session.get('cart', {})

    if stock > 0:
        cart[item_id] = stock
        messages.success(request,
                             (f'Updated {poster.name} '
                              f'stock to {cart[item_id]}'))
    else:
        bag.pop(item_id)
        messages.success(request,
                             (f'Removed {poster.name} from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
 
    try:
        poster = get_object_or_404(Poster, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request,
                             (f'Removed {poster.name} from your cart'))
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
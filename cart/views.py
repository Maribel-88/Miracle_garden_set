from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from gardensets.models import Gardenset 

# Create your views here.

def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    gardenset = get_object_or_404(Gardenset, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {gardenset.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {gardenset.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    """ Adjust the quantity of the specified property to the shopping cart """

    gardenset = get_object_or_404(Gardenset, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {gardenset.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {gardenset.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart """

    try:
        gardenset = get_object_or_404(Gardenset, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {gardenset.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    
    except Exception as e:
        messages.error(request,f'Error removing item: {e}')
        return HttpResponse(status=500)
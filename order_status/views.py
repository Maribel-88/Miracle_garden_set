from django.shortcuts import render, get_object_or_404

from checkout.models import Order

# Create your views here.

def order_status(request):
    """ A view to return the index page """
   
    return render(request, 'order_status/order_status.html')

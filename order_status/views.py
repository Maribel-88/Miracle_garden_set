from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from checkout.models import Order

# Create your views here.


def order_status(request):
    """ A view to return the index page """

    orderlists = Order.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "No search result")
            return redirect (reverse('order_status'))
        
        queries = Q(order_number__icontains=query) 
        orderlists = orderlists.filter(queries)

   
    context = {
        'orderlists': orderlists,
        'search_term': query,
    }
    return render(request, 'order_status/order_status.html', context)


    

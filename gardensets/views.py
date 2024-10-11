from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Gardenset

# Create your views here.

def all_garden_sets(request):
    """ A view to return all garden sets, including sorting and search queries """

    gardensets = Gardenset.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search result")
                return redirect (reverse('gardensets'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            gardensets = gardensets.filter(queries)


    context = {
        'gardensets': gardensets,
        'search_term': query,
    }
    return render(request, 'gardensets/gardensets.html', context)

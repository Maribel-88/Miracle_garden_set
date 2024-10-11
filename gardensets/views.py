from django.shortcuts import render
from .models import Gardenset

# Create your views here.

def all_garden_sets(request):
    """ A view to return all garden sets, including sorting and search queries """

    gardensets = Gardenset.objects.all()

    context = {
        'gardensets': gardensets,
    }
    return render(request, 'gardensets/gardensets.html', context)

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Gardenset, Category
from .forms import GardenForm

# Create your views here.

def all_garden_sets(request):
    """ A view to return all garden sets, including sorting and search queries """

    gardensets = Gardenset.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                gardensets = gardensets.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            gardensets = gardensets.order_by(sortkey)        

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            gardensets = gardensets.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search result")
                return redirect (reverse('gardensets'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            gardensets = gardensets.filter(queries)
    
    current_sorting = f'{sort}_{direction}'


    context = {
        'gardensets': gardensets,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'gardensets/gardensets.html', context)


def gardenset_detail(request, gardenset_id):
    """ A view that will return the details of the specific garden set """

    gardenset = get_object_or_404(Gardenset, pk=gardenset_id)

    context = {
        'gardenset': gardenset,
    }

    return render(request, 'gardensets/gardenset_detail.html', context)


@login_required
def add_gardenset(request):
    """ Add a new garden set to the store """
    if not request.user.is_superuser:
        messages.error(request, 'This action needs permission from admin')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GardenForm(request.POST, request.FILES)
        if form.is_valid():
            gardenset = form.save()
            messages.success(request, 'Successfully added new Garden set!')
            return redirect(reverse('add_gardenset'))
        else:
            message.error(request, 'Failed to add new item. Please ensure the form is valid.')
    else:
        form = GardenForm()
        
    template = 'gardensets/add_gardenset.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_gardenset(request, gardenset_id):
    """ Edit a garden set in the store """
    if not request.user.is_superuser:
        messages.error(request, 'This action needs permission from admin')
        return redirect(reverse('home'))

    gardenset = get_object_or_404(Gardenset, pk=gardenset_id)
    if request.method == 'POST':
        form = GardenForm(request.POST, request.FILES, instance=gardenset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the gardenset!')
            return redirect(reverse('gardenset_detail', args=[gardenset.id]))
        else:
            messages.error(request, 'Failed to update the garden set. Please ensure the form is valid.')
    else:
        form = GardenForm(instance=gardenset)
        messages.info(request, f'You are editing {gardenset.name}')

    template = 'gardensets/edit_gardenset.html'
    context = {
        'form': form,
        'gardenset': gardenset,
    }

    return render(request, template, context)


@login_required
def delete_gardenset(request, gardenset_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'This action needs permission from admin')
        return redirect(reverse('home'))
        
    gardenset = get_object_or_404(Gardenset, pk=product_id)
    gardenset.delete()
    messages.success(request, 'Garden set deleted!')
    return redirect(reverse('gardensets'))
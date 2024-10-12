from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_garden_sets, name='gardensets'),
    path('<gardenset_id>', views.gardenset_detail, name='gardenset_detail'),
]

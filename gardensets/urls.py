from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_garden_sets, name='gardensets'),
    path('<int:gardenset_id>/', views.gardenset_detail, name='gardenset_detail'),
    path('add/', views.add_gardenset, name='add_gardenset'),
]

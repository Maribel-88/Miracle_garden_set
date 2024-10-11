from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_garden_sets, name='gardensets')
]

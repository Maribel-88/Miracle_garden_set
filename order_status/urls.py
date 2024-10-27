from django.urls import path
from . import views 

urlpatterns = [
    path('', views.order_status, name='order_status'),
    path('refund/', views.refund_status, name='refund_status'),
]

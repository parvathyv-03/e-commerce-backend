from django.urls import path
from.views import create_order,get_orders

urlpatterns = [
    path('checkout/',create_order),
    path('my-orders/',get_orders),
]
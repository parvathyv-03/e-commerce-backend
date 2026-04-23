from django.urls import path
from.views import create_order

urlpatterns = [
    path('checkout/',create_order)
]
from django.urls import path
from .views import get_products,get_product_detail

urlpatterns = [
    path('products/',get_products),
    path('products/<slug:slug>/',get_product_detail)
]
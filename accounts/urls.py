from django.urls import path
from .views import signup
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import wishlist_view,cart_view

urlpatterns=[
    path('signup/',signup),
    path('login/',TokenObtainPairView.as_view()),   
    path('wishlist/',wishlist_view),
    path('cart/',cart_view),
]
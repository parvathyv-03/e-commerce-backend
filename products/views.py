from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def get_products(request):
    print("🔥🔥 VIEW HIT 🔥🔥")  
    category = request.GET.get('category')
    print(category)

    # filters products
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
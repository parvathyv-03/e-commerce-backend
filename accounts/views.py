#Django REST framework needs decorator 
from rest_framework.decorators import api_view
# User model already exists,so..
from django.contrib.auth.models import User

from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Wishlist,Cart
from products.models import Product
from django.shortcuts import get_object_or_404


# Create your views here.

# This function accepts POST requests
@api_view(['POST'])
def signup(request):
    # Read data from request,getting username,password from frontend
    username = request.data.get('username')
    password = request.data.get('password')

    # Username already exists or not
    if User.objects.filter(username=username).exists():
        return Response({"error":"User already exists"},status=400)
    
    # validate password
    try:
        validate_password(password)
    except ValidationError as e:
        return Response({"error":list(e.messages)},status=400)
    
    # if everything is valid
    User.objects.create_user(username=username,password=password)
    return Response({"message":"Signup Successful"})


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def wishlist_view(request):

    user =request.user

    # GET --> fetch wishlist
    if request.method == 'GET':
        items = Wishlist.objects.filter(user=user)

        data = []
        for item in items:
            data.append({
                "id":item.product.id,
                "name":item.product.name,
                "price":item.product.price,
                "image":item.product.image.url,
            })
        return Response(data)
    
    # POST --> add/remove (toggle)

    if request.method == 'POST':
        product_id = request.data.get("product_id")

        product = Product.objects.get(id=product_id)

        item = Wishlist.objects.filter(user=user,product=product).first()

        if item:
            item.delete()
            return Response({"message":"Removed from wishlist"})
        else:
            Wishlist.objects.create(user=user,product=product)
            return Response({"message":"Added to wishlist"})


@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def cart_view(request):

    # GET - Fetch Cart
    if request.method == 'GET':
        cart_items = Cart.objects.filter(user=request.user)

        data = []
        for item in cart_items:
            data.append({
                "id": item.product.id,
                "name": item.product.name,
                "price": item.product.price,
                "image": item.product.image.url if item.product.image else "",
                "quantity": item.quantity
            })
        return Response(data)
    
    # POST -- add/increase quantity
    if request.method == 'POST':
        product_id = request.data.get("product_id")

        if not product_id:
            return Response({"error": "product_id required"},status=400)
        
        product = get_object_or_404(Product,id=product_id)

        cart_item = Cart.objects.filter(user=request.user,product=product).first()

        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
            return Response({"message":"Quantity increased"})
        else:
            Cart.objects.create(user=request.user,product=product)
            return Response({"message":"Added to Cart"})
        
    # DELETE -- remove item

    if request.method == 'DELETE':
            product_id = request.data.get("product_id")

            product = get_object_or_404(Product,id=product_id)

            Cart.objects.filter(user=request.user,product=product).delete()

            return Response({"message":"Removed from cart"})
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import OrderSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    data = request.data

    serializer = OrderSerializer(data={
        **data,
        'user': request.user.id
    })

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors,status=400)
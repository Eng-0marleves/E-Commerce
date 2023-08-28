from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Wishlist
from .serializers import WishlistSerializer
from Products.models import Product


@api_view(['GET'])
def wishlist_products(request):
    req_states= status.HTTP_400_BAD_REQUEST
    user = request.user
    try:
        wishlist = Wishlist.objects.get(user=user)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(f'error in wishlist is => {e}')


@api_view(['POST'])
def add_to_wishlist(request):
    req_states= status.HTTP_400_BAD_REQUEST
    user = request.user
    product_id = request.data.get('product_id')
    
    try:
        product = Product.objects.get(id=product_id)
        wishlist, created = Wishlist.objects.get_or_create(user=user)
        wishlist.products.add(product)
        serializer = WishlistSerializer(wishlist)
        if serializer.is_valid():
            serializer.save()
            req_status = status.HTTP_201_CREATED
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(f'error in add_to_wishlist => {e}')

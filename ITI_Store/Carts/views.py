from django.shortcuts import render , redirect , get_object_or_404 
from django.http import HttpResponse
from Products.models import Category,Product
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer , CartItemSerializer
# Create your views here.

@api_view(['GET'])
def view_cart(request):
    req_status = status.HTTP_400_BAD_REQUEST
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart, many=True)
        req_status = status.HTTP_200_OK
        return Response(serializer.data)
    except Exception as e:
        print(f'error in all_book_api => {e}')    
@api_view(['POST'])
def add_to_cart(request, product_id):
    req_status = status.HTTP_400_BAD_REQUEST
    user = request.user
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.filter(user=user).first()  # Try to get existing cart
        
        if not cart:
            cart = Cart(user=user)
            cart.save()

        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        
        if not cart_item:
            cart_item = CartItem(cart=cart, product=product)
            cart_item.save()
        else:
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartSerializer(cart)

        if serializer.is_valid():
            serializer.save()
            req_status = status.HTTP_201_CREATED
        
    except Exception as e:
        print(f'error in add_to_cart => {e}')
        req_status = status.HTTP_404_NOT_FOUND

    return Response(serializer.data, status=req_status)

@api_view(['POST'])
def remove_from_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        serializer = CartSerializer(cart)
        
        req_status = status.HTTP_200_OK
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            req_status= status.HTTP_202_ACCEPTED
        else:
            cart_item.delete()
            req_status= status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(f'error in all_book_api => {e}')
    return Response(serializer.data,status=req_status)
    

@api_view(['DELETE'])
def clear_cart(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        cart.items.all().delete()
        req_status = status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(f'error in all_book_api => {e}')
    
    return Response({"message": "Cart cleared"})







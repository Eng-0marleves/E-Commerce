from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import Category,Product

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import Category_serializer,Product_serializer
# Create your views here.

@api_view(['GET'])
def All_product_api(request):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = Product.objects.all()
        product_serializer = Product_serializer(products, many=True).data
        data['products'] = product_serializer
        req_status = status.HTTP_200_OK
    except Exception as e:
        print(f'error in All_product_api => {e}')
    return Response(data=data, status=req_status)

#--------
@api_view(['GET'])
def All_product_name_api(request,name):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = Product.objects.filter(name__icontains=name)
        product_serializer = Product_serializer(products, many=True).data
        data['products'] = product_serializer
        req_status = status.HTTP_200_OK
    except Exception as e:
        print(f'error in All_product_name_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['GET'])
def All_product_id_api(request,id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = get_object_or_404(Product,id=id)
        product_serializer = Product_serializer(products, many=True).data
        data['products'] = product_serializer
        req_status = status.HTTP_200_OK
    except Exception as e:
        print(f'error in All_product_id_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['POST'])
def Add_product_api(request):
    req_status = status.HTTP_400_BAD_REQUEST
    data={}
    try:
        New_product = Product_serializer(data=request.data)
        if New_product.is_valid():
            New_product.save()
            data['New_product'] = New_product.data
            req_status = status.HTTP_201_CREATED
    except Exception as e:
        print(f'error in New_product_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['PUT'])
def Edit_product_api(request, id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = get_object_or_404(Product, id=id)
        x = Product_serializer(instance=products, data=request.data, partial=True)
        if x.is_valid():
            x.save()
            req_status = status.HTTP_200_OK
            data['products'] = x.data
    except Exception as e:
        print(f'error in Edit_product_api => {e}')
    return Response(data=data, status=req_status)


@api_view(['DELETE'])
def Delete_product_api(request, id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        products = get_object_or_404(book, id=id)
        product_serializer = Product_serializer(instance=products).data
        products.delete()
        req_status = status.HTTP_204_NO_CONTENT
        data['products'] = product_serializer
    except Exception as e:
        print(f'error in Delete_product_api => {e}')
    return Response(data=data, status=req_status)





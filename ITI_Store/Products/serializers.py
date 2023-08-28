from rest_framework import serializers
from .models import Category , Product

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','id')

class Product_serializer(serializers.ModelSerializer):
    Category = Category_serializer(read_only=True)
    Category_id = serializers.IntegerField(write_only=True)
    image = serializers.ImageField(use_url=True)  # Ensure use_url is set to True


    class Meta:
        model = Product
        fields = ("name",
            "description",
            "price",
            "brand",
            "image",
            "ratings",
            "stock",
            "createAt",
            "availabe",
            "Category",
            "Category_id")

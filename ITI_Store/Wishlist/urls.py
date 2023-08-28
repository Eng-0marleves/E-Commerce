from django.urls import path
from .views import wishlist_products, add_to_wishlist

urlpatterns = [
    # Your existing URLs
    path('api/wishlist/', wishlist_products, name='wishlist-products'),
    path('api/add-to-wishlist/', add_to_wishlist, name='add-to-wishlist'),
]

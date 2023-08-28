from django.urls import path
from . import views
from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart, clear_cart

urlpatterns = [
    #  _________________________ rest framework ________________________
    #path('api/all_products/', views.All_product_api, name='All_product-api'),

    path('api/view', view_cart, name='view_cart'),
    path('api/add_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('api/remove_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('api/clear_allcart/', clear_cart, name='clear_cart'),
]



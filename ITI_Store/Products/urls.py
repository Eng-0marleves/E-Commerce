from django.urls import path
from . import views

urlpatterns = [
    #  _________________________ rest framework ________________________



    path('api/all_products/', views.All_product_api, name='All_product-api'),
    path('api/all_products_id/<int:id>/search', views.All_product_id_api, name='All_product_id-api'),
    path('api/all_products_name/<str:name>/search', views.All_product_name_api, name='All_product_name-api'),
    path('api/delete_product/<int:id>/delete', views.Delete_product_api, name='Delete_product-api'),
    path('api/add_product/', views.Add_product_api, name='Add_product-api'),
    path('api/edit_product/', views.Edit_product_api, name='Edit_product-api'),


]
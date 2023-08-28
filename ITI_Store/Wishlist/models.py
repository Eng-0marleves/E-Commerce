from django.db import models
from django.contrib.auth.models import User
from Products.models import Product

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlist_products')

    def __str__(self):
        return str(self.id)
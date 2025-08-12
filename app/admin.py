from django.contrib import admin
from .models import Product, Cart, CartItem, Review, UserProfile, Order

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(UserProfile)
admin.site.register(Order)
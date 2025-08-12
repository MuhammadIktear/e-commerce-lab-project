from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/related/', views.related_products, name='related_products'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/', views.cart_add_item, name='cart_add_item'),
    path('cart/remove/<int:item_id>/', views.cart_remove_item, name='cart_remove_item'),
    path('cart/update/<int:item_id>/', views.cart_update_quantity, name='cart_update_quantity'),
    path('products/<int:product_id>/reviews/', views.product_reviews, name='product_reviews'),
    path('reviews/submit/', views.submit_review, name='submit_review'),
    path('reviews/featured/', views.featured_reviews, name='featured_reviews'),
    path('profile/', views.user_profile, name='user_profile'),
    path('auth/signup/', views.signup, name='signup'),
    path('auth/signin/', views.signin, name='signin'),
    path('orders/place/', views.place_order, name='place_order'),
]
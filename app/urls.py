from django.urls import path
from . import views

urlpatterns = [
    # Wilaya URLs
    path('wilayas/', views.wilaya_list, name='wilaya_list'),
    path('wilayas/create/', views.wilaya_create, name='wilaya_create'),
    path('wilayas/update/<int:id>/', views.wilaya_update, name='wilaya_update'),
    path('wilayas/delete/<int:id>/', views.wilaya_delete, name='wilaya_delete'),

    # Moughataa URLs
    path('moughataas/', views.moughataa_list, name='moughataa_list'),
    path('moughataas/create/', views.moughataa_create, name='moughataa_create'),
    path('moughataas/update/<int:id>/', views.moughataa_update, name='moughataa_update'),
    path('moughataas/delete/<int:id>/', views.moughataa_delete, name='moughataa_delete'),

    # Commune URLs
    path('communes/', views.commune_list, name='commune_list'),
    path('communes/create/', views.commune_create, name='commune_create'),
    path('communes/update/<int:id>/', views.commune_update, name='commune_update'),
    path('communes/delete/<int:id>/', views.commune_delete, name='commune_delete'),

    # PointDeVente URLs
    path('pointsdevente/', views.pointdevente_list, name='pointdevente_list'),
    path('pointsdevente/create/', views.pointdevente_create, name='pointdevente_create'),
    path('pointsdevente/update/<int:id>/', views.pointdevente_update, name='pointdevente_update'),
    path('pointsdevente/delete/<int:id>/', views.pointdevente_delete, name='pointdevente_delete'),

    # ProductType URLs
    path('producttypes/', views.producttype_list, name='producttype_list'),
    path('producttypes/create/', views.producttype_create, name='producttype_create'),
    path('producttypes/update/<int:id>/', views.producttype_update, name='producttype_update'),
    path('producttypes/delete/<int:id>/', views.producttype_delete, name='producttype_delete'),

    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:id>/', views.product_update, name='product_update'),
    path('products/delete/<int:id>/', views.product_delete, name='product_delete'),

    # Cart URLs
    path('carts/', views.cart_list, name='cart_list'),
    path('carts/create/', views.cart_create, name='cart_create'),
    path('carts/update/<int:id>/', views.cart_update, name='cart_update'),
    path('carts/delete/<int:id>/', views.cart_delete, name='cart_delete'),

    # CartProduct URLs
    path('cartproducts/', views.cartproduct_list, name='cartproduct_list'),
    path('cartproducts/create/', views.cartproduct_create, name='cartproduct_create'),
    path('cartproducts/update/<int:id>/', views.cartproduct_update, name='cartproduct_update'),
    path('cartproducts/delete/<int:id>/', views.cartproduct_delete, name='cartproduct_delete'),
]
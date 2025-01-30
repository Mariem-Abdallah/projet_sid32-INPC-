from django.urls import path
from . import views
from .views import export_wilayas_to_excel,import_wilayas_from_excel ,export_moughataas, import_moughataas,export_communes,import_communes ,export_pointdevente, import_pointdevente ,export_producttype, import_producttype ,export_product, import_product ,export_cart, import_cart ,export_cartproduct, import_cartproduct ,export_productprice, import_productprice
from .views import calculate_inpc
urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil

# URL pour calculer l'INPC

    path('calculate_inpc/', views.calculate_inpc, name='calculate_inpc'),
    
    # Wilaya URLs
    path('wilayas/', views.wilaya_list, name='wilaya_list'),
    path('wilayas/create/', views.wilaya_create, name='wilaya_create'),
    path('wilayas/update/<int:id>/', views.wilaya_update, name='wilaya_update'),
    path('wilayas/delete/<int:id>/', views.wilaya_delete, name='wilaya_delete'),
    path('wilayas/export/', export_wilayas_to_excel, name='export_wilayas'),
    path('wilayas/import/', import_wilayas_from_excel, name='import_wilayas'),



    # Moughataa URLs
    path('moughataas/', views.moughataa_list, name='moughataa_list'),
    path('moughataas/create/', views.moughataa_create, name='moughataa_create'),
    path('moughataas/update/<int:id>/', views.moughataa_update, name='moughataa_update'),
    path('moughataas/delete/<int:id>/', views.moughataa_delete, name='moughataa_delete'),
    path('moughataas/export/', export_moughataas, name='export_moughataas'),
    path('moughataas/import/', import_moughataas, name='import_moughataas'),

    # Commune URLs
    path('communes/', views.commune_list, name='commune_list'),
    path('communes/create/', views.commune_create, name='commune_create'),
    path('communes/update/<int:id>/', views.commune_update, name='commune_update'),
    path('communes/delete/<int:id>/', views.commune_delete, name='commune_delete'),
    path("communes/export/", export_communes, name="export_communes"),
    path("communes/import/", import_communes, name="import_communes"),


    # PointDeVente URLs
    path('pointsdevente/', views.pointdevente_list, name='pointdevente_list'),
    path('pointsdevente/create/', views.pointdevente_create, name='pointdevente_create'),
    path('pointsdevente/update/<int:id>/', views.pointdevente_update, name='pointdevente_update'),
    path('pointsdevente/delete/<int:id>/', views.pointdevente_delete, name='pointdevente_delete'),
    path('pointdevente/export/', export_pointdevente, name='export_pointdevente'),
    path('pointdevente/import/', import_pointdevente, name='import_pointdevente'),

    # ProductType URLs
    path('producttypes/', views.producttype_list, name='producttype_list'),
    path('producttypes/create/', views.producttype_create, name='producttype_create'),
    path('producttypes/update/<int:id>/', views.producttype_update, name='producttype_update'),
    path('producttypes/delete/<int:id>/', views.producttype_delete, name='producttype_delete'),
    path('producttype/export/', export_producttype, name='export_producttype'),
    path('producttype/import/', import_producttype, name='import_producttype'),

    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:id>/', views.product_update, name='product_update'),
    path('products/delete/<int:id>/', views.product_delete, name='product_delete'),
    path('product/export/', export_product, name='export_product'),
    path('product/import/', import_product, name='import_product'),
    # Cart URLs
    path('carts/', views.cart_list, name='cart_list'),
    path('carts/create/', views.cart_create, name='cart_create'),
    path('carts/update/<int:id>/', views.cart_update, name='cart_update'),
    path('carts/delete/<int:id>/', views.cart_delete, name='cart_delete'),
    path('cart/export/', export_cart, name='export_cart'),
    path('cart/import/', import_cart, name='import_cart'),

    # CartProduct URLs
    path('cartproducts/', views.cartproduct_list, name='cartproduct_list'),
    path('cartproducts/create/', views.cartproduct_create, name='cartproduct_create'),
    path('cartproducts/update/<int:id>/', views.cartproduct_update, name='cartproduct_update'),
    path('cartproducts/delete/<int:id>/', views.cartproduct_delete, name='cartproduct_delete'),
    path('cartproduct/export/', export_cartproduct, name='export_cartproduct'),
    path('cartproduct/import/', import_cartproduct, name='import_cartproduct'),

    # Prix URLs
   
    path('prix/', views.prix_list, name='prix_list'),
    path('prix/create/', views.prix_create, name='prix_create'),
    path('prix/update/<int:id>/', views.prix_update, name='prix_update'),
    path('prix/delete/<int:id>/', views.prix_delete, name='prix_delete'),
    path('productprice/export/', export_productprice, name='export_productprice'),
    path('productprice/import/', import_productprice, name='import_productprice'),
# URLs pour les structures administratives

    # URL pour la page de configuration
    path('structures/', views.structures_list, name='structures_list'),


]

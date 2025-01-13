from django import forms
from .models import Wilaya, Moughataa, Commune, PointDeVente, ProductType, Product, Cart, CartProduct

# Wilaya Form
class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ['code', 'name']

# Moughataa Form
class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = ['code', 'label', 'wilaya']

# Commune Form
class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['code', 'name', 'type', 'moughataa']

# PointDeVente Form
class PointDeVenteForm(forms.ModelForm):
    class Meta:
        model = PointDeVente
        fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']

# ProductType Form
class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['code', 'label', 'description']

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'unit_measure', 'product_type']

# Cart Form
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['code', 'name', 'description']

# CartProduct Form
class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['weight', 'value', 'date_from', 'date_to', 'product', 'point_of_sale']
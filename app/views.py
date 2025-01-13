from django.shortcuts import render, get_object_or_404, redirect
from .models import Wilaya, Moughataa, Commune, PointDeVente, ProductType, Product, Cart, CartProduct
from .forms import WilayaForm, MoughataaForm, CommuneForm, PointDeVenteForm, ProductTypeForm, ProductForm, CartForm, CartProductForm

# Wilaya Views
def wilaya_list(request):
 wilayas = Wilaya.objects.all() 
 return render(request, 'wilaya_list.html', {'wilayas': wilayas})

def wilaya_create(request):
    if request.method == 'POST':
        form = WilayaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wilaya_list')
    else:
        form = WilayaForm()
    return render(request, 'wilaya_form.html', {'form': form})

def wilaya_update(request, id):
    wilaya = get_object_or_404(Wilaya, id=id)
    if request.method == 'POST':
        form = WilayaForm(request.POST, instance=wilaya)
        if form.is_valid():
            form.save()
            return redirect('wilaya_list')
    else:
        form = WilayaForm(instance=wilaya)
    return render(request, 'app/wilaya_form.html', {'form': form})


def wilaya_delete(request, id):
    wilaya = get_object_or_404(Wilaya, id=id)
    if request.method == 'POST':
        wilaya.delete()
        return redirect('wilaya_list')
    return render(request, 'wilaya_confirm_delete.html', {'wilaya': wilaya})

# Moughataa Views
def moughataa_list(request):
    moughataas = Moughataa.objects.all()
    for m in moughataas:
        print(f"Moughataa ID: {m.id}")  # Vérifier si chaque objet a bien un ID
    return render(request, 'moughataa_list.html', {'moughataas': moughataas})

def moughataa_create(request):
    if request.method == 'POST':
        form = MoughataaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moughataa_list')
    else:
        form = MoughataaForm()
    return render(request, 'moughataa_form.html', {'form': form})

def moughataa_update(request, id):
    moughataa = get_object_or_404(Moughataa, id=id)
    if request.method == 'POST':
        form = MoughataaForm(request.POST, instance=moughataa)
        if form.is_valid():
            form.save()
            return redirect('moughataa_list')
    else:
        form = MoughataaForm(instance=moughataa)
    return render(request, 'moughataa_form.html', {'form': form})

def moughataa_delete(request, id):
    moughataa = get_object_or_404(Moughataa, id=id)
    if request.method == 'POST':
        moughataa.delete()
        return redirect('moughataa_list')
    return render(request, 'moughataa_confirm_delete.html', {'moughataa': moughataa})

# Commune Views
def commune_list(request):
    communes = Commune.objects.all()
    return render(request, 'commune_list.html', {'communes': communes})

def commune_create(request):
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commune_list')
    else:
        form = CommuneForm()
    return render(request, 'commune_form.html', {'form': form})

def commune_update(request, id):
    commune = get_object_or_404(Commune, id=id)
    if request.method == 'POST':
        form = CommuneForm(request.POST, instance=commune)
        if form.is_valid():
            form.save()
            return redirect('commune_list')
    else:
        form = CommuneForm(instance=commune)
    return render(request, 'commune_form.html', {'form': form})

def commune_delete(request, id):
    commune = get_object_or_404(Commune, id=id)
    if request.method == 'POST':
        commune.delete()
        return redirect('commune_list')
    return render(request, 'commune_confirm_delete.html', {'commune': commune})

# PointDeVente Views
def pointdevente_list(request):
    pointsdevente = PointDeVente.objects.all()
    return render(request, 'pointdevente_list.html', {'pointsdevente': pointsdevente})

def pointdevente_create(request):
    if request.method == 'POST':
        form = PointDeVenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pointdevente_list')
    else:
        form = PointDeVenteForm()
    return render(request, 'pointdevente_form.html', {'form': form})

def pointdevente_update(request, id):
    pointdevente = get_object_or_404(PointDeVente, id=id)
    if request.method == 'POST':
        form = PointDeVenteForm(request.POST, instance=pointdevente)
        if form.is_valid():
            form.save()
            return redirect('pointdevente_list')
    else:
        form = PointDeVenteForm(instance=pointdevente)
    return render(request, 'pointdevente_form.html', {'form': form})

def pointdevente_delete(request, id):
    pointdevente = get_object_or_404(PointDeVente, id=id)
    if request.method == 'POST':
        pointdevente.delete()
        return redirect('pointdevente_list')
    return render(request, 'pointdevente_confirm_delete.html', {'pointdevente': pointdevente})

# ProductType Views
def producttype_list(request):
    producttypes = ProductType.objects.all()
    return render(request, 'producttype_list.html', {'producttypes': producttypes})

def producttype_create(request):
    if request.method == 'POST':
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producttype_list')
    else:
        form = ProductTypeForm()
    return render(request, 'producttype_form.html', {'form': form})

def producttype_update(request, id):
    producttype = get_object_or_404(ProductType, id=id)
    if request.method == 'POST':
        form = ProductTypeForm(request.POST, instance=producttype)
        if form.is_valid():
            form.save()
            return redirect('producttype_list')
    else:
        form = ProductTypeForm(instance=producttype)
    return render(request, 'producttype_form.html', {'form': form})

def producttype_delete(request, id):
    producttype = get_object_or_404(ProductType, id=id)
    if request.method == 'POST':
        producttype.delete()
        return redirect('producttype_list')
    return render(request, 'producttype_confirm_delete.html', {'producttype': producttype})

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# Cart Views
def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart_list.html', {'carts': carts})

def cart_create(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartForm()
    return render(request, 'cart_form.html', {'form': form})

def cart_update(request, id):
    cart = get_object_or_404(Cart, id=id)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartForm(instance=cart)
    return render(request, 'cart_form.html', {'form': form})

def cart_delete(request, id):
    cart = get_object_or_404(Cart, id=id)
    if request.method == 'POST':
        cart.delete()
        return redirect('cart_list')
    return render(request, 'cart_confirm_delete.html', {'cart': cart})

# CartProduct Views
def cartproduct_list(request):
    cartproducts = CartProduct.objects.all()
    return render(request, 'cartproduct_list.html', {'cartproducts': cartproducts})

def cartproduct_create(request):
    if request.method == 'POST':
        form = CartProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartproduct_list')
    else:
        form = CartProductForm()
    return render(request, 'cartproduct_form.html', {'form': form})

def cartproduct_update(request, id):
    cartproduct = get_object_or_404(CartProduct, id=id)
    if request.method == 'POST':
        form = CartProductForm(request.POST, instance=cartproduct)
        if form.is_valid():
            form.save()
            return redirect('cartproduct_list')
    else:
        form = CartProductForm(instance=cartproduct)
    return render(request, 'cartproduct_form.html', {'form': form})

def cartproduct_delete(request, id):
    cartproduct = get_object_or_404(CartProduct, id=id)
    if request.method == 'POST':
        cartproduct.delete()
        return redirect('cartproduct_list')
    return render(request, 'cartproduct_confirm_delete.html', {'cartproduct': cartproduct})
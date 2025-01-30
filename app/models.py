from django.db import models

# Modèle pour Wilaya
class Wilaya(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=252)

    def __str__(self):
        return self.name

# Modèle pour Moughataa
class Moughataa(models.Model):
    code = models.CharField(max_length=45, unique=True)
    label = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

# Modèle pour Commune
class Commune(models.Model):
    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Modèle pour PointDeVente
class PointDeVente(models.Model):
    code = models.CharField(max_length=45, unique=True)
    type = models.CharField(max_length=45)
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

# Modèle pour ProductType
class ProductType(models.Model):
    code = models.CharField(max_length=45, unique=True)
    label = models.CharField(max_length=45)
    description = models.TextField()


    def __str__(self):
        return self.label

# Modèle pour Product
class Product(models.Model):
    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    description = models.TextField()
    unit_measure = models.CharField(max_length=45)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

# Modèle pour Cart
class Cart(models.Model):
    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.name

# Modèle pour CartProduct
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.product.name} - {self.point_of_sale.code}"

# Modèle pour ProductPrice
class ProductPrice(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   point_of_sale = models.ForeignKey(PointDeVente, on_delete=models.CASCADE)
   value = models.FloatField()
   date_from = models.DateField()
   date_to = models.DateField(null=True, blank=True)

   def __str__(self):
        return f"{self.product.name} - {self.value} - {self.date_from} à {self.date_to}"

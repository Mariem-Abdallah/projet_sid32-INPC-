from django.db import models

# Modèle pour Wilaya
class Wilaya(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

# Modèle pour Moughataa
class Moughataa(models.Model):
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

# Modèle pour Commune
class Commune(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Modèle pour PointDeVente
class PointDeVente(models.Model):
    code = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

# Modèle pour ProductType
class ProductType(models.Model):
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.label

# Modèle pour Product
class Product(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    unit_measure = models.CharField(max_length=45)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Modèle pour Cart
class Cart(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.name

# Modèle pour CartProduct
class CartProduct(models.Model):
    weight = models.FloatField()
    value = models.FloatField(default=1.1)  # Valeur par défaut
    date_from = models.DateField()
    date_to = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    point_of_sale = models.ForeignKey(PointDeVente, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.product.name} - {self.point_of_sale.code}"
from django.db import models

class ProductsCategory(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
    quantitiy = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products_image")

    caregory = models.ForeignKey(to = ProductsCategory, on_delete=models.CASCADE )

    #
    def __str__(self):
        return self.name

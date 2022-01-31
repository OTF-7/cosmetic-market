from django.db import models
from django.urls import reverse


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)

    # slug = models.SlugField(max_length=120, null=True)

    def __str__(self):
        return f"The brand name: {self.name}\n, " \
               f"The brand origin: {self.origin}\n"

    def get_absolute_url(self):
        return reverse("brands")


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=120, null=True)
    description = models.TextField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, models.CASCADE)

    def __str__(self):
        return f"The product name: {self.name}\n, " \
               f"The kind of the product: {self.kind}\n, " + \
               f"The description of the product: {self.description}\n, " + \
               f"The expire date of the product: {self.expire_date}\n, " + \
               f"The price of the product: {self.price}\n, " + \
               f"The brand name of the product: {self.brand.name}\n"

    def get_absolute_url(self):
        return reverse("products")

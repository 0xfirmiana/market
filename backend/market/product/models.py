from django.db import models
from seller.models import Seller

# Create your models here.
class Product(models.Model):

    name = models.CharField(name='name', blank=False, max_length=128)
    price = models.DecimalField(name='price', max_digits=6, blank=False, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name 
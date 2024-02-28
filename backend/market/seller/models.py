from django.db import models

# Create your models here.
class Seller(models.Model):

    name = models.CharField(name='name', max_length=32, null=False, unique=True, blank=False)
    logo = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name
from rest_framework import serializers
from .models import Seller 
from product.models import Product
from product.serializers import ProductSerializer

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name='all_products'
    ) 
    class Meta:
        model = Seller 
        fields = ['id', 'name', 'logo', 'products']
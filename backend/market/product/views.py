from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .models import Product
from .serializers import ProductSerializer

class all_products(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .models import Seller 
from .serializers import SellerSerializer

class all_sellers(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
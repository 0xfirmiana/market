from django.contrib import admin
from django.urls import path, include
from product.models import Product
from seller.models import Seller
from rest_framework import routers
from django.conf import settings 
from django.conf.urls.static import static

#admin.site.register(Product)
#admin.site.register(Seller)
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/seller/', include('seller.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

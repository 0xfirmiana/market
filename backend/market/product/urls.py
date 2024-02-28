from django.urls import path, include
from rest_framework import routers
from . import views
#from market.urls import router

router = routers.DefaultRouter()
router.register('all_products', views.all_products)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers
from . import views
from market.urls import router

router.register('all_sellers', views.all_sellers)

urlpatterns = [
    path('', include(router.urls)),
]
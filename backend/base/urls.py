from django.urls import path, include

from .views import VendorViewSet, PurchaseViewSet
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register("vendors", VendorViewSet)
router.register("purchase_orders", PurchaseViewSet)

urlpatterns = [
    path("", views.home, name="home"),
]

urlpatterns += router.urls

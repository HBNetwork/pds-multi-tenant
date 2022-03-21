from django.urls import include, path
from accounting.api.viewsets import VendorViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"vendors", VendorViewSet, basename="Vendors")

urlpatterns = [
    path("api/", include(router.urls)),
]

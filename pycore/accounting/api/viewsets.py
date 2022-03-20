from rest_framework.viewsets import ModelViewSet
from accounting.api.serializers import VendorSerializer

from accounting.models import Vendor

class VendorViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_fields = ('cnpj', 'corporate_name')

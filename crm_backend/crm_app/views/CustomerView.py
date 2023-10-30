from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .decorators import add_cors_headers
from ..models import Customer
from ..serializers import CustomerSerializer


# @method_decorator(add_cors_headers, name='dispatch')
@permission_classes([IsAuthenticated])
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

from rest_framework import viewsets
from ..models import SalesOpportunity
from ..serializers import SalesOpportunitySerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class SalesOpportunityViewSet(viewsets.ModelViewSet):
    queryset = SalesOpportunity.objects.all()
    serializer_class = SalesOpportunitySerializer
    

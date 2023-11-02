from rest_framework import serializers
from .models import Customer
from .models import SalesOpportunity


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOpportunity
        fields = '__all__'

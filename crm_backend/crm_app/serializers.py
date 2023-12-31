from rest_framework import serializers
from .models import Customer
from .models import SalesOpportunity
from .models import Task
from .models import Report


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOpportunity
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
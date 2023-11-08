from rest_framework import viewsets
from ..models import Task
from ..serializers import TaskSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone


@permission_classes([IsAuthenticated])
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def due_today_count(self, request):
        today = timezone.now().date()
        tasks_due_today = Task.objects.filter(due_date=today)
        count = tasks_due_today.count()
        return Response({'count': count})

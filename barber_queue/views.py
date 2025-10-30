from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta
from .models import Queue
from .serializers import QueueSerializer


class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all().order_by('-date')
    serializer_class = QueueSerializer
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['get'])
    def today(self, request):
        today_start = now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        qs = Queue.objects.filter(date__range=(today_start, today_end))
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

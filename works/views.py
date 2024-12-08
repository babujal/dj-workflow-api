from .models import WorkOrder
from rest_framework import viewsets, permissions
from .serializers import WorkOrderSerializer

# Create your views here.
class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset=WorkOrder.objects.all()
    serializer_class=WorkOrderSerializer
    permission_classes=[permissions.AllowAny]
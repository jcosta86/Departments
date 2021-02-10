from rest_framework import viewsets, generics
from .serializers import DepartmentSerializer, SectorSerializer, ListSectorByDepartmentSerializer
from .models import Department, Sector


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all().order_by('name')
    serializer_class = SectorSerializer

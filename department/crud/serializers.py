from rest_framework import serializers
from .models import Department, Sector


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class ListSectorByDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ['name', 'description']

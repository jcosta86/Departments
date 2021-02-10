from django.urls import include, path
from rest_framework import routers
from .views import DepartmentViewSet


router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet, basename="departments")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.urls import include, path
from rest_framework import routers
from .views import DepartmentViewSet, SectorViewSet, ListSectorByDepartment


router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet, basename="departments")
router.register('sectors', SectorViewSet, basename="sectors")


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('departments/<int:pk>/sectors/', ListSectorByDepartment.as_view()),
]

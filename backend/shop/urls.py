from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CheckAdminStatus

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('check-admin/', CheckAdminStatus.as_view(), name='check-admin'),
]
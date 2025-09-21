from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RifaViewSet, BilheteViewSet

router = DefaultRouter()
router.register(r'rifas', RifaViewSet, basename='rifa')
router.register(r'bilhetes', BilheteViewSet, basename='bilhete')

urlpatterns = [
    path('', include(router.urls)),
]
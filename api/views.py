from rest_framework import viewsets
from .models import Rifa, Bilhete
from .serializers import RifaSerializer, BilheteSerializer

class RifaViewSet(viewsets.ModelViewSet):
    queryset = Rifa.objects.all()
    serializer_class = RifaSerializer

class BilheteViewSet(viewsets.ModelViewSet):
    queryset = Bilhete.objects.all()
    serializer_class = BilheteSerializer
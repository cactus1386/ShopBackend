# views.py

from rest_framework import generics
from .models import Tshirt, Pant, sock
from .serializers import TshirtSerializer, PantSerializer

class TshirtListAPIView(generics.ListAPIView):
    queryset = Tshirt.objects.all()
    serializer_class = TshirtSerializer

class PantListAPIView(generics.ListAPIView):
    queryset = Pant.objects.all()
    serializer_class = PantSerializer
# Create your views here.
from rest_framework import generics

from .models import Corporation
from .models import Location
from .serializers import CorporationSerializer
from .serializers import LocationSerializer


class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CorporationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Corporation.objects.all()
    serializer_class = CorporationSerializer

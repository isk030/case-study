from django.urls import path

from .views import CorporationListCreateAPIView
from .views import LocationListCreateAPIView

app_name = "corporations"

urlpatterns = [
    path("locations/", LocationListCreateAPIView.as_view(), name="location-list-create"),
    path("corporations/", CorporationListCreateAPIView.as_view(), name="corporation-list-create"),
]

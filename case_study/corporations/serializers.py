from rest_framework import serializers

from .models import Corporation
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CorporationSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Corporation
        fields = "__all__"

from decimal import Decimal

from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status

from case_study.corporations.models import Location
from case_study.corporations.tests.base import CorporationsBaseTest


class LocationAPITests(CorporationsBaseTest):
    def setUp(self):
        super().setUp()

        self.location_data = {
            "corporation": self.corporation,
            "name": "Test Location",
            "street": "Hauptstraße 1",
            "zip_code": "12345",
            "country": "Test Country",
            "longitude": "12.345",
            "latitude": "98.765",
        }

        self.view_name = "corporations:location-list-create"

    def test_returns_empty_list_of_locations(self):
        response = self.client.get(reverse(self.view_name))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

    def test_creates_location(self):
        self.location_data["corporation"] = self.corporation.id
        response = self.client.post(reverse(self.view_name), self.location_data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert self.corporation.locations.count() == 1

        location = Location.objects.get(id=response.data["id"])
        for k, v in model_to_dict(location, fields=list(self.location_data.keys())).items():
            if isinstance(v, Decimal):
                assert v == Decimal(self.location_data[k])
            else:
                assert v == self.location_data[k]

    def test_returns_list_of_locations(self):
        Location.objects.create(**self.location_data)

        response = self.client.get(reverse(self.view_name))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

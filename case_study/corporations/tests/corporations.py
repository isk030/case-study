from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status

from case_study.corporations.models import Corporation
from case_study.corporations.models import Location
from case_study.corporations.tests.base import CorporationsBaseTest


class CorporationAPITests(CorporationsBaseTest):
    def setUp(self):
        super().setUp()

        self.new_corporation_data = {
            "name": "Test Corporation2",
            "description": "Test Description",
        }

        self.view_name = "corporations:corporation-list-create"

    def test_returns_400_due_to_existing_corporation(self):
        self.new_corporation_data["name"] = self.corporation.name
        response = self.client.post(
            reverse(self.view_name),
            self.new_corporation_data,
            format="json",
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_creates_corporation_without_locations(self):
        response = self.client.post(
            reverse(self.view_name),
            self.new_corporation_data,
            format="json",
        )

        corporation_id = response.data["id"]

        assert response.status_code == status.HTTP_201_CREATED

        assert Corporation.objects.filter(id=corporation_id).exists()

        for k, v in model_to_dict(
            Corporation.objects.get(id=corporation_id),
            fields=list(self.new_corporation_data.keys()),
        ).items():
            assert v == self.new_corporation_data[k]

    def test_returns_list_of_corporations_with_nested_location(self):
        new_corporation = Corporation.objects.create(**self.new_corporation_data)

        new_location_data = Location.objects.create(
            corporation=new_corporation,
            name="Test Location",
            street="Hauptstraße 1",
            zip_code="12345",
            country="Test Country",
            longitude="12.345",
            latitude="98.765",
        )

        response = self.client.get(reverse(self.view_name))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == Corporation.objects.count()

        for corporation_from_response in response.data:
            corporation_from_db = Corporation.objects.get(id=corporation_from_response["id"])
            assert corporation_from_db

            if corporation_from_response["locations"]:
                assert corporation_from_db.locations.count() == 1
                assert corporation_from_db.locations.first().id == new_location_data.id
            else:
                assert corporation_from_db.locations.count() == 0

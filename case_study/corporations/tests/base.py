from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from case_study.corporations.models import Corporation
from case_study.users.models import User


class CorporationsBaseTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.corporation = Corporation.objects.create(name="Test Corporation")

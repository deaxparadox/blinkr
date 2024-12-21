"""Testing dashboard"""

from django.test import TestCase
from django.shortcuts import redirect
from django.urls import reverse

class TestDashboard(TestCase):
    

    def test_simple_dashboard_response(self):
        client = self.client_class()
        client.login(
            username="paradox", 
            password= "13690000"
        )
        response = client.get(reverse("shortener:dashboard"))
        self.assertEqual(response.status_code, 200)
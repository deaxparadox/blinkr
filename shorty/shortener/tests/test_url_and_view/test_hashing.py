"""
Testing for hashing a new URLs.
"""

from django.test import Client
from django.urls import reverse
from django.shortcuts import redirect


def test_new_url_hashing(self):
    client = Client()
    client.post(reverse("shortener:hash"), {"full_url": "https://facebook.com/deaxparadox"})
    
    return 
from django.shortcuts import redirect
from django.urls import reverse
from django.test import TestCase, Client
from django.http import HttpResponse
from django.contrib.auth.models import User


from authentication.models import Authentication, Setting
from shortener.models import URL, URLEncodeMedium

# class TestShortenerIndex(TestCase):
#     def setUp(self) -> None:
#         self.url = "/shortener/"
#         self.reverse_url = reverse("shortener:index")
        
        
#     def test_shortener_index(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "_base.html")
#         self.assertTemplateUsed(response, "include/navbar.html")
#         self.assertTemplateUsed(response, "include/message.html")
#         self.assertTemplateUsed(response, "shortener/index.html")
#         print(response.context)
        
        

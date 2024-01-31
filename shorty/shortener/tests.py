from django.shortcuts import redirect
from django.urls import reverse
from django.test import TestCase


class IndexToShortenerIndexTestCase(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(reverse("index"))
    def test_redirect_from_index_to_shortener_index(self):
        self.assertEqual(self.response.status_code, 302)

class ShortenerIndexTextCase(TestCase):
    def test_shortener_index(self):
        response = self.client.get("http://localhost:8000/shortener/")
        self.assertEqual(response.status_code, 200)
    def test_shortener_index_reverse(self):
        response = self.client.get(reverse("shortener:index"))
        self.assertEqual(response.status_code, 200)

class ShortenerIndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("http://localhost:8000/shortener/")
        
    def test_template_shortener_base(self):
        self.assertTemplateUsed(self.response, "shortener/_base.html")

    def test_template_shortener_indexGeneric(self):
        # print(self.response.context)
        self.assertTemplateUsed(self.response, "shortener/index_generic.html")
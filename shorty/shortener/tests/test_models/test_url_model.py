from django.test import TestCase
from shortener.models import URL, URLEncodeMedium


class TestURLModel(TestCase):
    def setUp(self):
        self.new_url = URL.objects.create(full_url="https://google.com/1", medium=URLEncodeMedium.NORMAL)
        
    def test_new_url_instance(self):
        self.assertEqual(self.new_url.active, True)
        self.assertEqual(self.new_url.delete, False)
        self.assertEqual(self.new_url.clicks, 0)
        self.assertEqual(self.new_url.visibility, 1)
        self.assertEqual(self.new_url.visibility.value, 1)
        self.assertEqual(self.new_url.visibility.name, "PUBLIC")
        
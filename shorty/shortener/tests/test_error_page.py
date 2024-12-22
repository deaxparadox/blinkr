from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By

class TestError(StaticLiveServerTestCase):
    def setUp(self):
        return super().setUp()
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

from authentication.utils.test.user import Testuser

# 1. Test session expire time. (Set SESSION_COOKIE_AGE = 60, before running this test)

class TestLoginExpireTime(StaticLiveServerTestCase):
    # fixtures = ["user-data.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
        

    # This function test the functionality of the session cookie,
    # cookie expries in 60s, after which user will automatically
    # logged out. Then user have to login again.
    def test_expire_time(self):
        Testuser.create_user()
        
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:login")}")
        username_input = self.selenium.find_element(By.ID, "login-username")
        username_input.send_keys(Testuser.username)
        password_input1 = self.selenium.find_element(By.ID, "login-password")
        password_input1.send_keys(Testuser.password1)
        self.selenium.find_element(By.CLASS_NAME, 'login-button').click()
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("shortener:dashboard")}"
        )
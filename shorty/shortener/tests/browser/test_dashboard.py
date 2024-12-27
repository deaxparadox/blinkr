from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

from authentication.utils.test.user import Testuser



class TestLogin(StaticLiveServerTestCase):
    # fixtures = ["user-data.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)



    # Logged in user redirect to dashboard.
    def test_login_redirect_dashboard(self):
        
        # user created
        Testuser.create_user()
        
        self.selenium.get(
            "%s%s" % (self.live_server_url, reverse("authentication:login"))
        );
        
                
        username_input = self.selenium.find_element(By.ID, "login-username")
        username_input.send_keys(Testuser.username)
        
        password_input = self.selenium.find_element(By.ID, "login-password")
        password_input.send_keys(Testuser.password1)
        
        self.selenium.find_element(By.CLASS_NAME, 'login-button').click()
        
        
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("shortener:dashboard")}"
        )
        
        sleep(3)
        
    # Logged in user redirect to dashboard.
    def test_login_redirect_query_string(self):
        
        # user created
        Testuser.create_user()
        
        self.selenium.get(
            "%s%s" % (self.live_server_url, reverse("authentication:login"))
        )
        
                
        username_input = self.selenium.find_element(By.ID, "login-username")
        username_input.send_keys(Testuser.username)
        
        password_input = self.selenium.find_element(By.ID, "login-password")
        password_input.send_keys(Testuser.password1)
        
        self.selenium.find_element(By.CLASS_NAME, 'login-button').click()
        
        
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("shortener:dashboard")}"
        )
        
        sleep(3)
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

from authentication.utils.test.user import Testuser


# DONE
# 1. Test new user login.
# 2. Test user login of not registered user, redirect to register page.
# 3. Test incorrect user name as password.
# 4. Authenticated (logged in) user try to register.
# 5. Authenticated (logged in) user try to login again.


class TestLogin(StaticLiveServerTestCase):
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
        

    # This function login the new user.
    def test_login(self):
        # creating the new user.
        Testuser.create_user()
        
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:login")}")
        
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
        
    
    # This function test for user login,
    # for user which does not exists.
    def test_login_user_does_not_exist(self):
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:login")}")
        
        username_input = self.selenium.find_element(By.ID, "login-username")
        username_input.send_keys(Testuser.username)
        
        password_input = self.selenium.find_element(By.ID, "login-password")
        password_input.send_keys(Testuser.password1)
        
        self.selenium.find_element(By.CLASS_NAME, 'login-button').click()
        
        
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("authentication:register")}"
        )
        
        sleep(3)
        
    # This function test for incorrect username and password.
    def test_login_incorrect_username_and_password(self):
        
        # creating the new user.
        Testuser.create_user()
        
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:login")}")
        
        username_input = self.selenium.find_element(By.ID, "login-username")
        username_input.send_keys(Testuser.username)
        
        password_input = self.selenium.find_element(By.ID, "login-password")
        password_input.send_keys(Testuser.password2)
        
        self.selenium.find_element(By.CLASS_NAME, 'login-button').click()
        
        
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("authentication:login")}"
        )
        
        sleep(3)
      
    # 4. Authenticated (logged in) user try to register.
    # This function test for authenticated user trying to 
    # register will be redirected to dashboard.
    def test_login_loggedin_retry_register(self):
        
        # creating the new user.
        Testuser.create_user()
        
        
        # login
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:login")}")
        username_input = self.selenium.find_element(By.ID, "login-username")
        username_input.send_keys(Testuser.username)
        password_input = self.selenium.find_element(By.ID, "login-password")
        password_input.send_keys(Testuser.password1)
        self.selenium.find_element(By.CLASS_NAME, 'login-button').click()
        
        # user will be dashboard
        self.assertEqual(
            self.selenium.current_url,
            f"{self.live_server_url}{reverse("shortener:dashboard")}?last=no&short_active=no"
        )
        
        # try to register
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:register")}")
        
        # will be redirect to dashboard
        self.assertEqual(
            self.selenium.current_url,
            f"{self.live_server_url}{reverse("shortener:dashboard")}?last=no&short_active=no"
        )
        
        sleep(3)
        
    # 4. Authenticated (logged in) user try to login again.
    # This function test for authenticated user trying to 
    # login will be redirected to dashboard.
    def test_login_loggedin_retry_login(self):
        
        # creating the new user.
        Testuser.create_user()
        
        
        sleep(1)
        # login
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:login")}")
        username_input = self.selenium.find_element(By.ID, "login-username")
        username_input.send_keys(Testuser.username)
        password_input = self.selenium.find_element(By.ID, "login-password")
        password_input.send_keys(Testuser.password1)
        self.selenium.find_element(By.CLASS_NAME, 'login-button').click()

        # user will be dashboard
        self.assertEqual(
            self.selenium.current_url,
            f"{self.live_server_url}{reverse("shortener:dashboard")}?last=no&short_active=no"
        )
        
        sleep(1)
        # try to register
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:login")}")
        
        # will be redirect to dashboard
        self.assertEqual(
            self.selenium.current_url,
            f"{self.live_server_url}{reverse("shortener:dashboard")}?last=no&short_active=no"
        )
        
        sleep(3)
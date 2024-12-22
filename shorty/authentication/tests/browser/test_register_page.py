from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

from authentication.utils.test.user import Testuser

class TestRegister(StaticLiveServerTestCase):
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
        

    # This function register the new user.
    def test_new_registration(self):
        """
        Register a new user and redirect to login page.
        """
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:register")}")
        
        username_input = self.selenium.find_element(By.ID, "register-username")
        username_input.send_keys(Testuser.username)
        
        password_input1 = self.selenium.find_element(By.ID, "register-password1")
        password_input1.send_keys(Testuser.password1)
        
        password_input2 = self.selenium.find_element(By.ID, "register-password2")
        password_input2.send_keys(Testuser.password1)
        
        self.selenium.find_element(By.CLASS_NAME, 'register-button').click()
        
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("authentication:login")}"
        )
        sleep(3)
        
        

    # This test will test the functionality of the registration,
    # system, new user details will be sent to the server,
    # with different password, returning to registration page,
    # with response, containing message "Password doesn't match".
    def test_new_registration_different_password_fail(self):
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:register")}")
        
        username_input = self.selenium.find_element(By.ID, "register-username")
        username_input.send_keys(Testuser.username)
        
        password_input1 = self.selenium.find_element(By.ID, "register-password1")
        password_input1.send_keys(Testuser.password1)
        
        password_input2 = self.selenium.find_element(By.ID, "register-password2")
        password_input2.send_keys(Testuser.password2)
        
        self.selenium.find_element(By.CLASS_NAME, 'register-button').click()
        
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("authentication:register")}"
        )
        sleep(3)
    
    
    # This function test the functionality of the registration.
    # Try to register a existing user, will be redirected to login page,
    # returning response with message user already exists.
    def test_new_registration_already_registered_user(self):
        Testuser.create_user()
        
        self.selenium.get(f"{self.live_server_url}{reverse("authentication:register")}")
        
        username_input = self.selenium.find_element(By.ID, "register-username")
        username_input.send_keys(Testuser.username)
        
        password_input1 = self.selenium.find_element(By.ID, "register-password1")
        password_input1.send_keys(Testuser.password1)
        
        password_input2 = self.selenium.find_element(By.ID, "register-password2")
        password_input2.send_keys(Testuser.password1)
        
        self.selenium.find_element(By.CLASS_NAME, 'register-button').click()
        
        self.assertEqual(
            self.selenium.current_url, 
            f"{self.live_server_url}{reverse("authentication:login")}"
        )
        sleep(3)
from django.test import TestCase
from django.contrib.auth.models import User

from authentication.models import Authentication, Setting, AccountDeactivateChoices
from shortener.models import  VisibilityChoices


class TestSettingModel(TestCase):
    def setUp(self):
        self.new_settings = Setting.objects.create()
        
    # test new instance
    def test_new_instance(self):
        self.assertIsInstance(self.new_settings, Setting, "Checking new instance creation of Setting Model.")
        
    # testing default value of Account Deactivate
    def test_defualt_visiblity_value(self):
        self.assertEqual(self.new_settings.account_deactivate, AccountDeactivateChoices.NO, "Testing the default account deactivate.")
        self.assertEqual(self.new_settings.account_deactivate.value, AccountDeactivateChoices.NO.value, "Testing the default account deactivate.")
        self.assertEqual(self.new_settings.account_deactivate.value, 0, "Testing the default account deactivate.")

class TestAuthenticationModel(TestCase):
    def setUp(self):
        # settings up new user
        self.new_user = User.objects.create_user(username="testuser", password="136900")

        # settings up new setting
        self.new_set = Setting.objects.create()
        
    def test_new_authentication(self):
        new_auth = Authentication.objects.create(
            user=self.new_user,
            setting=self.new_set
        )
        self.assertIsInstance(new_auth, Authentication, "Teting new instance of Authentication.")
        self.assertEqual("testuser", new_auth.user.username)
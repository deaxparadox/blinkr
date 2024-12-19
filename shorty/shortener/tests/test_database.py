from django.test import TestCase
from django.contrib.auth.models import User


from authentication.models import Authentication, Setting
from ..models import URL, URLEncodeMedium

        
# URL models has ForeignKey to authentication.
# Testing the working of ForeignKey.
# 
# Authentication Account can point to mulitple
# URLs, but URLs can only have one ForeignKey.
class URLForeignKeyTest(TestCase):
    def test_add_mulitple_hashed_url(self):
        new_user = User.objects.create(username="nitish", password="136900")
        new_setting = Setting.objects.create()
        new_auth = Authentication.objects.create(user=new_user, setting=new_setting)
        
        new_url1 = URL.objects.create(full_url="https://google.com/1", medium=URLEncodeMedium.NORMAL)
        new_url2 = URL.objects.create(full_url="https://google.com/2", medium=URLEncodeMedium.NORMAL)
        
        new_auth.url.add(new_url1)
        new_auth.url.add(new_url2)
        new_auth.save()
        
        self.assertEqual(len(new_auth.url.all()), 2)
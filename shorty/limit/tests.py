from django.test import TestCase
from datetime import datetime
from django.conf import settings

from limit.models import Limit

class TestLimit(TestCase):
    def test_new_instance(self):
        """Test the new instance of the Limit Model"""
        l = Limit.objects.create()
        t = datetime.now()
        
        
        # default time
        self.assertEqual(l.cur.year, t.year)
        self.assertEqual(l.cur.day, t.day)
        self.assertEqual(l.cur.hour, t.hour)
        self.assertEqual(l.cur.min, t.min)
        self.assertEqual(l.cur.second, t.second)
        # self.assertEqual(l.cur.microsecond, t.microsecond)
        
        # default add
        self.assertEqual(l.remote_addr, '0.0.0.0')
        
        # default request
        self.assertEqual(l.total, 0)
        
        
class TestLimitIncrement(TestCase):
    obj: Limit | None = None
    obj_id: int | None = None
    
    @classmethod
    def setUp(cls):
        super().setUp(cls)
        cls.obj = Limit.objects.create()
        cls.obj_id = cls.obj.pk

        
    @classmethod
    def get_object(cls):
        cls.obj = Limit.objects.get(pk=cls.obj_id)
        
    def test_req_increment_method(self):
        self.assertEqual(self.obj.total, 0)
        self.obj.increment()
        self.obj.save()
        self.assertEqual(self.obj.total, 1)
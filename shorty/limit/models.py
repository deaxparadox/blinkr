from django.db import models
from datetime import datetime

# Total: 4 req in 2 seconds
# Request limit
REQ_LIMIT = 4
# Time limit
TIME_LIMIT = 2      

class Limit(models.Model):
    total = models.BigIntegerField(verbose_name="Total request made.", default=0)
    cur = models.DateTimeField(auto_now=True)
    remote_addr = models.CharField(max_length=15, verbose_name="Remote host address.", blank=True, default="0.0.0.0")
    
    def save(self, *args, request = None, remote: bool = False, **kwargs):
        if remote and request:
            self.remote_addr = Limit.get_remote_addr(request)
        return super().save(*args, **kwargs)
    
    def increment(self):
        self.total += 1
    
    
    """
    The time limit between the request should be 1 seconds.
        
    If the request is made within the 1 seconds, thne 
    `HttpResponse` with exceeds request limit will be sent.
    """
    @staticmethod
    def time_limit(instance, cur: datetime):
        pass
    
    @staticmethod
    def get_remote_addr(request) -> str:
        """
        Extract and return the remote host address from the request.
        """
        return request.META['REMOTE_ADDR']
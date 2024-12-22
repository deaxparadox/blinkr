from django.contrib.auth.models import User


class Testuser:
    username = "testuser1"
    password1 = "13690000"
    password2 = "23690000"
    password3 = "33690000"
    
    @classmethod        
    def create_user(cls):
        """
        This function create a new test user.
        
        class variable username and password1 are used.
        """
        User.objects.create_user(username=cls.username, password=cls.password1)
        
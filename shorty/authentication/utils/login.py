from django.contrib.auth.models import User
from authentication.forms import LoginForm, RegisterForm

class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    def login(self):
        return
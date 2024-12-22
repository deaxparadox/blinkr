from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
import logging

from . import forms
from .models import Authentication, Setting
from shortener.models import URL





logger = logging.getLogger(__name__)
# log_enable = True

# Shortcut for logging
def shortcut_logger(message, level = "Warning"):
    global logger
    # if level == "Warning":
    logger.warning(message)
    # return 
    

# Shortcut for messaging
message_enable = True
def shortcut_message(_request, level=messages.INFO, message: str = None):
    if message_enable:
        messages.add_message(_request, level, message)


# Shortcut for register view
def shortcut_register_view(request, message:str = None, pre_data=None):
    """
    This function is shortcut for generating register response, with message and 
    registration details.
    
    - message: Pass a message to display to user.
    
    - pre_data: This argument should only be used, 
    if login failed, then return the pre-filled details 
    in reponse except password.
    """
    if message is not None:
        shortcut_message(request, message=message)
        
    if pre_data is not None:
        register_form = forms.RegisterForm(pre_data)
    else:
        register_form = forms.RegisterForm()
        
    return render(
        request,
        "authentication/register.html",
        {
            "register_form": register_form
        }
    )


# Short for rederning login view
def shortcut_login_view(request, message:str = None, pre_data=None):
    """
    This function is shortcut for generating login response, with message and 
    login details.
    
    - message: Pass a message to display to user.
    
    - pre_data: This argument should only be used, 
    if login failed, then return the pre-filled details 
    in reponse except password.
    """
    
    
    # If message is passed.
    if message is not None:
        shortcut_message(request, message=message)
        
    # If POST request data is passed.
    if pre_data is not None:
        login_form = forms.LoginForm(pre_data)
    else:
        login_form = forms.LoginForm()
        
    # Return to login page.
    return render(
        request,
        "authentication/login.html",
        {
            "login_form": login_form
        }
    )


def check_existing_object(KClass = None, username: str = None) -> bool:
    """
    This function check user existence, if user exists 
    return True else return False.
    """
    try:
        get_list_or_404(klass=KClass, username=username)
    except Http404:
        return False
    return True


# Login view
def login_view(request):
    
    # Check to request type.
    if request.method == "POST":
        login_form_data = forms.LoginForm(request.POST)
        
        # Check if the form is valid,
        # if form is valid, authenticate and login the
        # user, else redirect to login page.
        if login_form_data.is_valid():
            
            username = login_form_data.cleaned_data['username']
            password = login_form_data.cleaned_data['password']
            
            # Check user existence, if user does not exist,
            # redirect to register page.
            if not check_existing_object(User, username=username):
                shortcut_message(request, message="User not registered.")
                return redirect(reverse("authentication:register"))
            
            
            # Authenticate the login user.
            user = authenticate(request, username=username, password=password)
            
            # 
            if user is not None:
                # If is authenticated,
                # login and redirect to index page.
                login(request, user)
                shortcut_message(request, messages.INFO, message="Login successfull.")
                return redirect(reverse("shortener:dashboard"))
            else:
                # If user is not authenticated,
                # redirect to login.
                return shortcut_login_view(request, message="Invalid username or password.", pre_data=request.POST)
                # return redirect(reverse("authentication:login"))
        else:
            # If login data is invalid return login page.
            return shortcut_login_view(request, message="Invalid username or password.", instance=login_form_data)
    
    
    return shortcut_login_view(request)





# Register view, register the new user.
def register_view(request):
    shortcut_logger("Register view")
    
    # Check the request type
    if request.method == "POST":
        shortcut_logger("POST request")
        
        # extract the form page.
        register_form_data = forms.RegisterForm(request.POST)
        shortcut_logger("Extract form data")
        
        # check user registration data validity.
        if register_form_data.is_valid():
            shortcut_logger("Valid user registration data")
            
            username: str = register_form_data.cleaned_data['username']
            password1: str = register_form_data.cleaned_data['password1']
            password2: str = register_form_data.cleaned_data['password2']
            
            # Lowercase the username and validate username.
            if (username == " " or username == "" or username is None):
                return shortcut_register_view(request, message="Invalid username.", pre_data=request.POST)
            try:
                username = username.lower()
            except Exception as e:
                return shortcut_register_view(request, message="Invalid username.", pre_data=request.POST)
            
            
            # Check both password1 and password.
            if password1 != password2:
                return shortcut_register_view(request, message="Password doesn't matched", pre_data=request.POST)
            
            
            # Checking existing user.
            if check_existing_object(User, username=username):
                shortcut_message(request, message="User already exists.")
                return redirect(reverse("authentication:login"))
            

            # Create new user.
            # If any exception is raise,
            # return to registration page.
            try:
                # registering new user
                new_user = User.objects.create_user(username=username, password=password1)
                new_setting = Setting.objects.create()
                Authentication.objects.create(user=new_user, setting=new_setting)
                
                shortcut_logger("User registered.")
                
            except Exception(e) as e:
                shortcut_logger("Error while creating new user.")
                
                # if exception is raise
                # to register page.
                return shortcut_register_view(request, e)
            
            shortcut_logger("New user registered, returning to login page.")
            
            # if user is successfull register,
            # return to login page.
            shortcut_message(request, message="User successfully registered.")
            return redirect(reverse("authentication:login"))
        
        else:    
            # If register form is invalid, 
            # go to register page.
            return shortcut_register_view(request, message="Password doesn't matched", pre_data=request.POST)
    
    shortcut_logger("GET request")
    return shortcut_register_view(request)




# Logout page view
def logout_view(request):
    return render(
        request,
        "authentication/logout.html"
    )
    
# logout view
def logout_request_view(request):
    logout(request)
    return redirect(reverse("authentication:login"))
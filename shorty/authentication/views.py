from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
import logging

from . import forms
from .models import Authentication, Setting
from shortener.models import URL





logger = logging.getLogger(__name__)
log_enable = False

# Shortcut for logging
def shortcut_logger(message, level = "Warning"):
    if log_enable:
        if level == "Warning":
            logger.warning(message)
        return 
    

# Shortcut for messaging
message_enable = True
def shortcut_message(_request, level=messages.INFO, message: str = None):
    if message_enable:
        messages.add_message(_request, level, message)


# Shortcut for register view
def shortcut_register_view(request, message:str = None, pre_data=None):
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
# 
def shortcut_login_view(request, message:str = None, pre_data=None):
    
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
            
            # Authenticate the login user.
            user = authenticate(request, username=username, password=password)
            
            # 
            if user is not None:
                # If is authenticated,
                # login and redirect to index page.
                login(request, user)
                shortcut_message(request, messages.INFO, message="Login successfull.")
                return redirect(reverse("shortener:index"))
            else:
                # If user is not authenticated,
                # redirect to login.
                return shortcut_login_view(request, message="Invalid username or password.", data=request.POST)
                return redirect(reverse("authentication:login"))
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
            
            username = register_form_data.cleaned_data['username']
            password1 = register_form_data.cleaned_data['password1']
            password2 = register_form_data.cleaned_data['password2']
            
            # If both password are same,
            # proceed to next step.
            if password1 == password2:
                shortcut_logger("Password1 and password2 matched.")
                
                # Create new user, if any exception is raise,
                # return register page.
                # 
                try:
                    # registering new user
                    new_user = User.objects.create_user(username=username, password=password1)
                    new_setting = Setting.objects.create()
                    Authentication.objects.create(user=new_user, setting=new_setting)
                    
                    shortcut_logger("New user created.")
                    
                except Exception(e) as e:
                    shortcut_logger("Error while creating new user.")
                    
                    # if exception is raise
                    # to register page.
                    return shortcut_register_view(request, e)
                
                shortcut_logger("New user registered, returning to login page.")
                
                # if user is successfull register,
                # return to login page.
                return shortcut_login_view(request)
            
            else:
                # If password1 and password doesnot match.
                # to register page.
                return shortcut_register_view(request, message="Password doesn't matched", pre_data=request.POST)
            
        # If register form is invalid, 
        # go to register page.
        return redirect(reverse("authentication:register"))
    
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
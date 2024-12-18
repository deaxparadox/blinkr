from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        help_text="Enter your username",
        widget=forms.TextInput(
            attrs={
                "id": "login-username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"id":'login-password'}),
    )
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=120,
        help_text="Enter your username",
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                "id": "register-username"
            }
        )
        
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"id":'register-password1'}),
        help_text="Password must contain atleast 8 digits.",
        max_length=120,
        min_length=8,
        
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"id":'register-password2'}),
        help_text="Password must contain atleast 8 digits.",
        max_length=120,
        min_length=8,
        
    )
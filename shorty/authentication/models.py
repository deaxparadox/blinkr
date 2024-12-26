from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.urls import reverse



class AccountDeactivateChoices(models.IntegerChoices):
    NO = 0, _("No")
    YES = 1, _("Yes")

    

class Setting(models.Model):
    account_deactivate = models.IntegerField(
        default=AccountDeactivateChoices.NO, 
        help_text="Account deactivate choices.",
        choices=AccountDeactivateChoices
    )
    
    
class Authentication(models.Model):
    setting = models.OneToOneField(
        Setting,
        null=True,
        blank=True,
        related_name="authentication", 
        on_delete=models.CASCADE
    )
    user = models.OneToOneField(
        User, 
        null=True, 
        blank=True, 
        related_name="authentication", 
        on_delete=models.CASCADE
    )
    # url = models.ForeignKey(
    #     URL, 
    #     related_name="authentication", 
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    
    @classmethod
    def get_absolute_login_redirect_url(
        self,
        request,
        redirect_to: str | None = None
    ):
        """
        This function create absolute URL for redirection from login.
        
        request: Request request.
        
        redirect_to: URL for redirection.
        """
        
        # HTTP VERSION
        http_scheme: str = request.scheme
        
        # SERVER ADDR
        http_host: str = request.META.get("HTTP_HOST")
        
        # PATH
        path: str | None = None
        
        return "%s?redirect_to=%s" % (
            reverse("authentication:login"),
            redirect_to
        )
    
    def __str__(self) -> str:
        return f"{self.user.username}"
    def __repr__(self) -> str:
        return self.__str__()
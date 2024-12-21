from hashlib import md5
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

from authentication.models import Authentication


class VisibilityChoices(models.IntegerChoices):
    PRIVATE = 0, _("No")
    PUBLIC = 1, _("Yes")


class URLEncodeMedium(models.IntegerChoices):
    NORMAL = 1, _("Normal")
    API = 2, _("API")
    GRAPHQL = 3, _("GraphQL")
    

def hash_url(url: str = None) -> str:
    """
    This function encode the long url in short 10 characters.
    """
    return md5(url.encode()).hexdigest()[:10]

class URL(models.Model):
    full_url = models.URLField(unique=True)                         # Original URL
    url_hash = models.URLField(unique=True, blank=True)             # Hashed URL
    clicks = models.IntegerField(default=0)                         # Total access count.
    created = models.DateTimeField(auto_now_add=True)               # Creation time.
    
    # Medium through which the Hash it created.
    medium = models.IntegerField(choices=URLEncodeMedium)
    
    # Activate or deactivate a URL
    active = models.BooleanField(default=True)
    
    # Delete the URLs
    delete = models.BooleanField(default=False)
    
    # Set visibility of the URLs,
    # If visibility is set to PUBLIC, a URL will be
    # available on the dashboard, else if the 
    # visibility is set to PRIVATE, it will displayed
    # to the owner in dashboard.
    visibility = models.IntegerField(
        default=VisibilityChoices.PUBLIC, 
        choices=VisibilityChoices, 
        help_text="Set visiblity of the Hashed URL."
    )
    
    # Many to one relation to Authencation Models.
    authentication = models.ForeignKey(
        Authentication,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="url"
    )
    
    def medium_name(self):
        return URLEncodeMedium(self.medium).name
    
    def get_absolute_url(self):
        return reverse("shortener:access", kwargs={"url_hash": self.url_hash})
    
    def clicked(self):
        self.clicks +=1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = hash_url(self.full_url)

        """
        First, this code instantiates the `URLValidator` 
        in the validate variable. Inside the `try/except` 
        block, you `validate()` the URL received and raise 
        a `GraphQLError` with the `invalid url` custom message 
        if something went wrong.
        """
        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            raise GraphQLError("invalid url")

        return super().save(*args, **kwargs)
    
    
    
    def __str__(self):
        return self.full_url
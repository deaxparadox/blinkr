from hashlib import md5
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from graphql import GraphQLError


class URLEncodeMedium(models.IntegerChoices):
    NORMAL = 1, _("Normal")
    API = 2, _("API")
    GRAPHQL = 3, _("GraphQL")
    
class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True, blank=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    medium = models.IntegerField(choices=URLEncodeMedium)
    
    def medium_name(self):
        return URLEncodeMedium(self.medium).name
    
    def get_absolute_url(self):
        return reverse("shortener:access", kwargs={"url_hash": self.url_hash})
    
    def clicked(self):
        self.clicks +=1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

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
from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag("shortener/tag/history.html")
def load_url_history(request):
    
    username = request.user.username
    user: User = User.objects.get(username=username)
    urls = user.authentication.url.all()
    
    return { 
        "urls": urls,
        "request_scheme": request.scheme,
        "request_http_host": request.META.get("HTTP_HOST"),
    }

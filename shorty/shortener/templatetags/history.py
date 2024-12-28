from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag("shortener/templates/history.html")
def load_url_history(request):
    username = request.user.username
    user: User = User.objects.get(username=username)
    
    urls = user.authentication.url.all()
    
    return {"urls": urls}
    
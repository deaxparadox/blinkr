from django import template

register = template.Library()

    
    
@register.simple_tag(takes_context=True)
def build_absolute_url(request, url):
    print(request)
    return request.build_absolute_ur(url)
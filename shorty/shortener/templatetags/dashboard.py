from django import template

register = template.Library()

@register.simple_tag
def load_query_string(request, **kwargs):
    query_string = request.GET.copy()
    query_string.clear()
    query_string.update(kwargs)
    return query_string.urlencode()
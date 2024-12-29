from django import template



register = template.Library()


# Anonymous formtag
@register.inclusion_tag("shortener/tag/anonymous_hash_form.html")
def anonymous_hash_form():
    return {}

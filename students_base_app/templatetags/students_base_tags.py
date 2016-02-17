from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit(obj):
    """
    Return Admin edit link for current object
    """
    return reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=(obj.id,))

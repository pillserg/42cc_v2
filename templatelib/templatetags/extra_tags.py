from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(obj):
    """
    getting parts from obj.__class__ and
    constructing url to admin page for this object
    """

    reverse_str = "admin:%s_%s_change" % (obj._meta.app_label,
                                      obj._meta.module_name)
    try:
        return reverse(reverse_str, args=(obj.pk,))
    except Exception:
        return ''

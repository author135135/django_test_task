from django import template
from django.core.urlresolvers import reverse, resolve, Http404

register = template.Library()


@register.simple_tag
def edit(obj):
    """
    Return Admin edit link for current object
    """
    return reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=(obj.id,))


@register.inclusion_tag('students_base_app/templatetags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    links = []

    url_path = context.request.path

    while url_path:
        try:
            resolver = resolve(url_path)

            title = resolver.url_name.replace('_', ' ').capitalize()

            link_data = {
                'title': title,
                'href': url_path,
            }

            if not links:
                link_data.pop('href')

            links.insert(0, link_data)
        except Http404:
            pass

        url_path = url_path.rstrip('/')

        if not url_path:
            break

        url_path = url_path[:url_path.rfind('/') + 1]

    return {
        'links': links
    }

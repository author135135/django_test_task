from django.conf import settings


def settings_processor(request):
    context = {
        'settings': settings
    }

    return context

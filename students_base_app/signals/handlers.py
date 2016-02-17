from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.admin.models import LogEntry
from students_base_app.models import ModelsLogger


@receiver([post_save, post_delete])
def models_action_logger(sender, **kwargs):
    if sender not in (ModelsLogger, LogEntry):

        if kwargs.get('created', None) is not None:
            action_type = 'create' if kwargs['created'] else 'update'
        else:
            action_type = 'delete'

        instance = kwargs['instance']

        ModelsLogger.log(instance._meta.app_label, instance._meta.model_name, action_type)

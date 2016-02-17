from django.db import models


# Create your models here.
class GroupManager(models.Manager):
    def get_queryset(self):
        return super(GroupManager, self).get_queryset().select_related('group_monitor').prefetch_related('student_set')


class Student(models.Model):
    full_name = models.CharField(max_length=75)
    birthdate = models.DateField()
    studentid_cart = models.CharField(max_length=25, blank=True)
    group = models.ForeignKey(to='Group')

    def __unicode__(self):
        return self.full_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.studentid_cart:
            try:
                student_id = self.id or (Student.objects.latest('id').id + 1)
            except Student.DoesNotExist:
                student_id = 1

            self.studentid_cart = u'{}-{}'.format(self.group.group_name, student_id)

        super(Student, self).save(force_insert, force_update, using, update_fields)


class Group(models.Model):
    group_name = models.CharField(max_length=25)
    group_monitor = models.ForeignKey(to=Student, related_name='+', blank=True, null=True, default=None)

    object = GroupManager()

    def __unicode__(self):
        return self.group_name

    def get_group_monitor(self):
        return self.group_monitor.full_name if self.group_monitor else 'Group monitor not assigned.'

    get_group_monitor.short_description = 'Group monitor'

    def _students_count(self):
        return self.student_set.count()

    students_count = property(_students_count)


class ModelsLogger(models.Model):
    OPERATION_TYPES = (
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete')
    )

    application = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    operation_type = models.CharField(max_length=15, choices=OPERATION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Model <{}:{}> Operation type: {}'.format(self.application, self.model, self.operation_type)

    @staticmethod
    def log(application, model_name, operation_type):
        instance = ModelsLogger(application=application, model=model_name, operation_type=operation_type)
        instance.save()

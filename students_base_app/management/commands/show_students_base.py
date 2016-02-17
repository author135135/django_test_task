from __future__ import unicode_literals
from django.core.management import BaseCommand
from students_base_app.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        output = ''

        if Group.objects.exists():
            for group in Group.objects.all():
                output += 'Group: {}'.format(group.group_name)

                for student in group.student_set.all():
                    output += '\nStudent: {}'.format(student.full_name)

                output += '\n\n'

            output = output[:-2]
        else:
            output = 'No groups found'

        print output

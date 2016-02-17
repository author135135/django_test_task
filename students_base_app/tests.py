from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
from students_base_app.models import Group, Student


# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        # Create user for test
        username = 'admin'
        password = User.objects.make_random_password()

        user = User(username=username)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)

        user.save()

        self.user_username = username
        self.user_password = password

    def test(self):
        """
        In this test we need to login in site(if required) and create group with student from site forms.
        """
        group_add_url = reverse('students_app:group_add')
        student_add_url = reverse('students_app:student_add')

        client = Client()

        # Check if login required and try login if need
        response = client.get(group_add_url)

        if response.status_code in (301, 302):
            response = client.login(username=self.user_username, password=self.user_password)

            self.assertTrue(response, 'Login in system: FAIL')

        # Create new group in site
        new_group_data = {
            'group_name': 'test-group-{}'.format(date.today().year)
        }

        client.post(group_add_url, new_group_data)

        try:
            group = Group.objects.get(group_name=new_group_data['group_name'])
        except Group.DoesNotExist:
            self.fail('Group create: FAIL')

        # `studentid_cart` generate automatically
        new_student_data = {
            'full_name': 'Tom Hardy',
            'birthdate': '1977-09-15',
            'group': group.id,
        }

        client.post(student_add_url, new_student_data)

        try:
            student = Student.objects.get(full_name=new_student_data['full_name'], group=group)
        except Student.DoesNotExist:
            self.fail('Student create: FAIL')

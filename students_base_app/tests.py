from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
from students_base_app.models import Group, Student


# Create your tests here.
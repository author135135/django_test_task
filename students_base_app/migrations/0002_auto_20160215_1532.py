# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentid_cart',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_base_app', '0002_auto_20160215_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('operation_type', models.CharField(max_length=15, choices=[(b'create', b'Create'), (b'update', b'Update'), (b'delete', b'Delete')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

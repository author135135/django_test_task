# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=75)),
                ('photo', models.ImageField(upload_to=b'students')),
                ('birthdate', models.DateField()),
                ('studentid_cart', models.CharField(max_length=25, blank=True)),
                ('group', models.ForeignKey(to='students_base_app.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='group_monitor',
            field=models.ForeignKey(related_name='+', default=None, blank=True, to='students_base_app.Student', null=True),
        ),
    ]

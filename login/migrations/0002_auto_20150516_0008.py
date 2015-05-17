# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='age',
            new_name='enroll',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='Male', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]

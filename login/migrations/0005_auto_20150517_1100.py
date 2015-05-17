# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_profile_enroll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cover_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]

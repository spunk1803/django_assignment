# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20150517_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_pic',
            field=models.ImageField(default='', upload_to=b'login/photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='', upload_to=b'login/photos/'),
            preserve_default=False,
        ),
    ]

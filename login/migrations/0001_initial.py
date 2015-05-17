# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('branch', models.CharField(max_length=30)),
                ('about', models.TextField()),
                ('profile_pic', models.ImageField(upload_to=b'login/photos/')),
                ('cover_pic', models.ImageField(upload_to=b'login/photos/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

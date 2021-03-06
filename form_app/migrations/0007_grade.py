# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0006_auto_20170502_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acaname', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6_\xe9\x99\xa2')),
                ('stuid', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6_\xe5\x8f\xb7')),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93_\xe5\x90\x8d')),
                ('grade1', models.CharField(max_length=50, verbose_name=b'\xe8\x8b\xb1_\xe8\xaf\xad')),
                ('grade2', models.CharField(max_length=50, verbose_name=b'\xe9\xab\x98_\xe6\x95\xb0')),
                ('grade3', models.CharField(max_length=50, verbose_name=b'\xe5\xa4\xa7_\xe7\x89\xa9')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

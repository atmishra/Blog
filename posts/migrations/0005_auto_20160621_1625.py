# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160621_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.date(2016, 6, 21), null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-28 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender_spot',
            name='status',
            field=models.CharField(default='open', max_length=250),
        ),
    ]

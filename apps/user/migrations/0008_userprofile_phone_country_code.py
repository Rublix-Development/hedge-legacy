# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20180130_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_country_code',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]

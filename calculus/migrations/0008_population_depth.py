# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculus', '0007_auto_20171126_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='population',
            name='depth',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

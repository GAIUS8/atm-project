# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculus', '0003_auto_20171125_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

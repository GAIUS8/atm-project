# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculus', '0006_population_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_snyc_date', models.DateField()),
                ('execution_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'update_record',
            },
        ),
        migrations.AlterIndexTogether(
            name='population',
            index_together=set([('name', 'season')]),
        ),
    ]

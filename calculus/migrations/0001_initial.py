# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('round', models.IntegerField(unique=True)),
                ('date_local', models.DateField()),
                ('num1', models.IntegerField()),
                ('num2', models.IntegerField()),
                ('num3', models.IntegerField()),
                ('num4', models.IntegerField()),
                ('num5', models.IntegerField()),
                ('num6', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('first_win', models.IntegerField()),
                ('second_win', models.IntegerField()),
                ('third_win', models.IntegerField()),
                ('fourth_win', models.IntegerField()),
                ('last_win', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181117_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='description',
            field=models.TextField(default='', verbose_name='Descripción'),
        ),
    ]

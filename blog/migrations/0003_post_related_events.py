# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-02 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20180701_1912'),
        ('blog', '0002_post_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='related_events',
            field=models.ManyToManyField(blank=True, related_name='posts', to='events.Event'),
        ),
    ]

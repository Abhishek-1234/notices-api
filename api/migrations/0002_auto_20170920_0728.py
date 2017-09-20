# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 07:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api',
            old_name='task_name',
            new_name='notice_author',
        ),
        migrations.RenameField(
            model_name='api',
            old_name='task_desc',
            new_name='notice_desc',
        ),
        migrations.RenameField(
            model_name='api',
            old_name='task_created',
            new_name='notice_publish_date',
        ),
        migrations.AddField(
            model_name='api',
            name='notice_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='api',
            name='notice_valid_till',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

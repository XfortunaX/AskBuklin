# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ask_buk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='dislike_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='dislike_count',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_count',
            field=models.IntegerField(default=0, verbose_name='Answer count'),
            preserve_default=False,
        ),
    ]

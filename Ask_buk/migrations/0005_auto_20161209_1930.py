# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ask_buk', '0004_auto_20161206_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='Like count'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_count',
            field=models.IntegerField(default=0, verbose_name='Answer count'),
        ),
        migrations.AlterField(
            model_name='question',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='Like count'),
        ),
    ]

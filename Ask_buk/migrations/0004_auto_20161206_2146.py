# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ask_buk', '0003_auto_20161206_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='uploads/', verbose_name='Avatar'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ask_buk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ask_buk.Question'),
            preserve_default=False,
        ),
    ]
